//
//  HomeView.swift
//  GestureLabIOS
//
//  Created by Aravind Badiger on 30/10/25.
//

import SwiftUI
import AVFoundation
import CoreLocation
import UserNotifications
import Photos
import UIKit

/// PermissionManager handles requesting the permissions sequentially
final class PermissionManager: NSObject, ObservableObject {
    // Published states for UI if you want to show status
    @Published var cameraAuthorized: Bool = false
    @Published var locationAuthorized: Bool = false
    @Published var notificationsAuthorized: Bool = false
    @Published var photosAuthorized: Bool = false

    private var locationManager: CLLocationManager?
    private var locationCompletion: ((Bool) -> Void)?

    override init() {
        super.init()
    }

    // MARK: - Public sequencing API

    /// Starts the sequence: Camera -> Location -> Notifications -> Photos
    func startPermissionSequence(completion: (() -> Void)? = nil) {
        requestCamera { [weak self] _ in
            guard let self = self else { return }
            self.requestLocation { _ in
                self.requestNotifications { _ in
                    self.requestPhotos { _ in
                        completion?()
                    }
                }
            }
        }
    }

    // MARK: - Camera (AVCapture)

    func requestCamera(completion: @escaping (Bool) -> Void) {
        switch AVCaptureDevice.authorizationStatus(for: .video) {
        case .authorized:
            DispatchQueue.main.async {
                self.cameraAuthorized = true
                completion(true)
            }
        case .notDetermined:
            AVCaptureDevice.requestAccess(for: .video) { granted in
                DispatchQueue.main.async {
                    self.cameraAuthorized = granted
                    completion(granted)
                }
            }
        default:
            // denied / restricted
            DispatchQueue.main.async {
                self.cameraAuthorized = false
                completion(false)
            }
        }
    }

    // MARK: - Location (CLLocationManager)

    func requestLocation(completion: @escaping (Bool) -> Void) {
        let status = CLLocationManager.authorizationStatus()
        switch status {
        case .authorizedAlways, .authorizedWhenInUse:
            self.locationAuthorized = true
            completion(true)
        case .notDetermined:
            self.locationManager = CLLocationManager()
            self.locationManager?.delegate = self
            self.locationCompletion = completion
            self.locationManager?.requestWhenInUseAuthorization()
        default:
            // denied / restricted
            self.locationAuthorized = false
            completion(false)
        }
    }

    // MARK: - Notifications (UNUserNotificationCenter)

    func requestNotifications(completion: @escaping (Bool) -> Void) {
        let center = UNUserNotificationCenter.current()
        center.getNotificationSettings { settings in
            switch settings.authorizationStatus {
            case .authorized, .provisional, .ephemeral:
                DispatchQueue.main.async {
                    self.notificationsAuthorized = true
                    completion(true)
                }
            case .notDetermined:
                center.requestAuthorization(options: [.alert, .sound, .badge]) { granted, _ in
                    DispatchQueue.main.async {
                        self.notificationsAuthorized = granted
                        completion(granted)
                    }
                }
            default:
                DispatchQueue.main.async {
                    self.notificationsAuthorized = false
                    completion(false)
                }
            }
        }
    }

    // MARK: - Photos / Gallery (PHPhotoLibrary)

    func requestPhotos(completion: @escaping (Bool) -> Void) {
        // Use the iOS 14+ API that accepts read/write scope to avoid deprecation warnings
        let status = PHPhotoLibrary.authorizationStatus(for: .readWrite)
        switch status {
        case .authorized, .limited:
            DispatchQueue.main.async {
                self.photosAuthorized = true
                completion(true)
            }
        case .notDetermined:
            PHPhotoLibrary.requestAuthorization(for: .readWrite) { newStatus in
                DispatchQueue.main.async {
                    let allowed = (newStatus == .authorized || newStatus == .limited)
                    self.photosAuthorized = allowed
                    completion(allowed)
                }
            }
        default:
            DispatchQueue.main.async {
                self.photosAuthorized = false
                completion(false)
            }
        }
    }

    // Helper to open Settings
    func openSettings() {
        guard let url = URL(string: UIApplication.openSettingsURLString) else { return }
        if UIApplication.shared.canOpenURL(url) {
            UIApplication.shared.open(url, options: [:], completionHandler: nil)
        }
    }
}

// MARK: - CLLocationManagerDelegate
extension PermissionManager: CLLocationManagerDelegate {
    func locationManagerDidChangeAuthorization(_ manager: CLLocationManager) {
        let status = CLLocationManager.authorizationStatus()
        switch status {
        case .authorizedAlways, .authorizedWhenInUse:
            locationAuthorized = true
            locationCompletion?(true)
            locationCompletion = nil
            locationManager = nil
        case .denied, .restricted:
            locationAuthorized = false
            locationCompletion?(false)
            locationCompletion = nil
            locationManager = nil
        default:
            break
        }
    }
}

struct HomeView: View {
    // Keep the existing demo items unchanged
    let items: [(String, AnyView)] = [
        ("Single Tap", AnyView(SingleTapView())),
        ("Double Tap", AnyView(DoubleTapView())),
        ("Tap and Hold", AnyView(LongPressView())),
        ("Drag and Drop", AnyView(DragAndDropView())),
        ("Swipe/Scroll", AnyView(SwipeScrollView())),
        ("No Internet", AnyView(NoInternetView())),
        ("Multi-Touch", AnyView(MultiTouchView())),
        ("Web-View", AnyView(WebViewLoadingView()))
    ]

    @StateObject private var permissionManager = PermissionManager()
    @State private var didRequestPermissions = false
    @State private var showingDeniedAlert = false
    @State private var deniedPermissionName: String = ""
    @State private var sequenceComplete = false

    var body: some View {
        List {
            ForEach(Array(items.enumerated()), id: \.offset) { idx, pair in
                NavigationLink(destination: pair.1) {
                    VStack(alignment: .leading) {
                        Text(pair.0).font(.headline)
                        Text("Open demo").font(.subheadline).foregroundColor(.gray)
                    }
                }
                .accessibilityIdentifier("nav_\(pair.0.replacingOccurrences(of: " ", with: "_"))")
            }
        }
        .navigationTitle("Home")
        .accessibilityIdentifier("home_list")
        .onAppear {
            // Preserve current behavior — only start permission flow once
            guard !didRequestPermissions else { return }
            didRequestPermissions = true

            // Start permission sequence in background
            permissionManager.startPermissionSequence {
                DispatchQueue.main.async {
                    sequenceComplete = true
                }
            }

            // Small delay then check for denied permissions to show a friendly alert
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.7) {
                checkForDeniedPermissions()
            }
        }
        .alert(isPresented: $showingDeniedAlert, content: {
            Alert(
                title: Text("\(deniedPermissionName) permission required"),
                message: Text("Please enable \(deniedPermissionName) in Settings to use this feature."),
                primaryButton: .default(Text("Open Settings"), action: {
                    permissionManager.openSettings()
                }),
                secondaryButton: .cancel(Text("Later"))
            )
        })
    }

    /// Small helper to check statuses and show alerts for the first denied permission found.
    private func checkForDeniedPermissions() {
        if !permissionManager.cameraAuthorized {
            deniedPermissionName = "Camera"
            showingDeniedAlert = true
            return
        }
        if !permissionManager.locationAuthorized {
            deniedPermissionName = "Location"
            showingDeniedAlert = true
            return
        }
        if !permissionManager.notificationsAuthorized {
            deniedPermissionName = "Notifications"
            showingDeniedAlert = true
            return
        }
        if !permissionManager.photosAuthorized {
            deniedPermissionName = "Photos"
            showingDeniedAlert = true
            return
        }
        // If we get here, nothing denied (or all allowed)
        sequenceComplete = true
    }
}

struct HomeView_Previews: PreviewProvider {
    static var previews: some View {
        HomeView()
    }
}
