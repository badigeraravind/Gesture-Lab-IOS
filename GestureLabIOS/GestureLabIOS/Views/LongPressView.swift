//
//  Untitled 3.swift
//  GestureLabIOS
//
//  Created by Aravind Badiger on 30/10/25.
//

import SwiftUI

struct LongPressView: View {
    @State private var showGift = false

    var body: some View {
        VStack {
            Spacer()
            if showGift {
                Text("🎁").font(.system(size: 80)).accessibilityIdentifier("gift_image")
                Spacer().frame(height: 12)
            }
            LongPressButton(label: "Preview", holdMillis: 2_000) {
                showGift = true
            }
            .accessibilityIdentifier("btn_preview")
            Spacer()
        }
        .padding()
        .navigationTitle("Tap and Hold")
    }
}

struct LongPressButton: View {
    let label: String
    let holdMillis: Int
    var onLongEnough: () -> Void

    @GestureState private var pressing = false

    var body: some View {
        Text(label)
            .padding(.horizontal, 24)
            .padding(.vertical, 12)
            .background(Color.accentColor)
            .foregroundColor(.white)
            .cornerRadius(24)
            .gesture(
                LongPressGesture(minimumDuration: Double(holdMillis) / 1000.0)
                    .onEnded { _ in onLongEnough() }
            )
    }
}
