//
//  GestureLabIOSApp.swift
//  GestureLabIOS
//
//  Created by Aravind Badiger on 30/10/25.
//

import SwiftUI

@main
struct GestureLabApp: App {
    @StateObject private var touchStore = GlobalTouchStore.shared
    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(touchStore)
        }
    }
}
