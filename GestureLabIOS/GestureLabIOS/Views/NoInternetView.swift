//
//  Untitled 6.swift
//  GestureLabIOS
//
//  Created by Aravind Badiger on 30/10/25.
//

import SwiftUI
import Network

struct NoInternetView: View {
    @StateObject private var monitor = NetworkMonitor()
    
    var body: some View {
        VStack {
            Spacer()
            
            // Status text (unchanged behavior)
            Text(monitor.isConnected ? "Internet Connected" : "connecting...waiting for internet")
                .font(.title2)
                .foregroundColor(monitor.isConnected ? .green : .red)
                .accessibilityIdentifier("internet_status")
            
            Spacer()
            
            // DEBUG: simulate network loss button area
            // Show "Simulate network loss" when not simulating, otherwise show "STOP"
            if monitor.isSimulating {
                Button("STOP") {
                    monitor.stopSimulation()
                }
                .padding(.horizontal, 24)
                .padding(.vertical, 12)
                .background(Color.red)
                .foregroundColor(.white)
                .cornerRadius(10)
                .accessibilityIdentifier("stop_button")
            } else {
                Button("Simulate network loss") {
                    monitor.startSimulation()
                }
                .padding(.horizontal, 20)
                .padding(.vertical, 12)
                .background(Color.blue)
                .foregroundColor(.white)
                .cornerRadius(10)
                .accessibilityIdentifier("simulate_button")
            }
            
            Spacer()
        }
        .navigationTitle("No Internet")
        .accessibilityIdentifier("no_internet")
    }
}


/// NetworkMonitor: publishes `isConnected` but can be forced offline via simulate flag.
/// Keeps the real NWPathMonitor behaviour and overlays simulation when requested.
final class NetworkMonitor: ObservableObject {
    // Published value that your UI binds to.
    @Published private(set) var isConnected: Bool = false
    
    // Expose whether simulation is active (so the UI knows which button to show)
    @Published private(set) var isSimulating: Bool = false
    
    // internal actual network state tracked from NWPathMonitor
    private var actualConnected: Bool = false {
        didSet { refreshPublishedState() }
    }
    
    // NWPathMonitor
    private var monitor = NWPathMonitor()
    
    init() {
        // path update handler updates `actualConnected`. UI gets `isConnected`
        monitor.pathUpdateHandler = { [weak self] path in
            guard let self = self else { return }
            DispatchQueue.main.async {
                self.actualConnected = (path.status == .satisfied)
            }
        }
        
        let q = DispatchQueue(label: "NetworkMonitor")
        monitor.start(queue: q)
    }
    
    deinit {
        monitor.cancel()
    }
    
    // MARK: - Simulation control
    
    /// Start simulating network loss. Published `isConnected` will become `false`.
    func startSimulation() {
        DispatchQueue.main.async {
            self.isSimulating = true
            self.refreshPublishedState()
        }
    }
    
    /// Stop simulation and revert to real network state.
    func stopSimulation() {
        DispatchQueue.main.async {
            self.isSimulating = false
            self.refreshPublishedState()
        }
    }
    
    /// Recompute and publish the `isConnected` state depending on simulation flag.
    private func refreshPublishedState() {
        // If simulating: always false. Otherwise use actualConnected.
        let newValue = isSimulating ? false : actualConnected
        // Only set the published property if value changed to avoid extra UI churn
        if isConnected != newValue {
            isConnected = newValue
        }
    }
}
