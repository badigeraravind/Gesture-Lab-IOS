//
//  ContentView.swift
//  GestureLabIOS
//
//  Created by Aravind Badiger on 30/10/25.
//

import SwiftUI

struct ContentView: View {
    @EnvironmentObject var touchStore: GlobalTouchStore
    @State private var path: [String] = []

    var body: some View {
        NavigationStack(path: $path) {
            LoginView(navPath: $path)
                .navigationDestination(for: String.self) { value in
                    if value == "home" {
                        HomeView()
                    }
                }
        }
        .overlay(
            ZStack {
                ForEach(Array(touchStore.activeTouches.keys), id: \.self) { key in
                    if let pt = touchStore.activeTouches[key] {
                        Circle()
                            .fill(Color(red: 0.09, green: 0.47, blue: 0.82))
                            .frame(width: 36, height: 36)
                            .position(pt)
                            .opacity(0.9)
                    }
                }
            }
            .allowsHitTesting(false)
        )
        .background(TouchCaptureView().environmentObject(touchStore))
    }
}
