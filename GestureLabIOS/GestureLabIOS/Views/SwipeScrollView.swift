//
//  Untitled 5.swift
//  GestureLabIOS
//
//  Created by Aravind Badiger on 30/10/25.
//

import SwiftUI

struct SwipeScrollView: View {
    var body: some View {
        VStack(spacing: 16) {
            Text("Swipe left/right the cards below")
            TabView {
                ForEach(0..<3) { i in
                    RoundedRectangle(cornerRadius: 20)
                        .fill([Color.green.opacity(0.6), Color.red.opacity(0.6), Color.blue.opacity(0.6)][i])
                        .overlay(Text("Page \(i+1)").font(.largeTitle).bold())
                        .padding(.horizontal, 16)
                }
            }
            .tabViewStyle(.page(indexDisplayMode: .automatic))
            .frame(height: 200)
            .accessibilityIdentifier("swipe_pager")

            Text("Scroll the list below")
            List(1...30, id: \.self) { i in
                Text("Item \(i)")
            }
            .accessibilityIdentifier("scroll_list")
        }
        .navigationTitle("Swipe / Scroll")
    }
}
