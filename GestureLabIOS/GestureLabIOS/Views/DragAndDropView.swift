//
//  Untitled 4.swift
//  GestureLabIOS
//
//  Created by Aravind Badiger on 30/10/25.
//

import SwiftUI

struct DragAndDropView: View {
    // offset is the current position of the nail
    @State private var offset = CGSize.zero
    // lastOffset stores the offset after gesture end so we accumulate translations
    @State private var lastOffset = CGSize.zero
    // whether initial centering has been done
    @State private var initialized = false

    var body: some View {
        GeometryReader { geo in
            ZStack {
                // light background to give context
                Color(red: 0.98, green: 0.97, blue: 0.95)
                    .edgesIgnoringSafeArea(.all)

                // draggable nail
                Circle()
                    .fill(Color(red: 0.55, green: 0.43, blue: 0.39))
                    .frame(width: 64, height: 64)
                    .overlay(
                        Circle()
                            .stroke(Color.black.opacity(0.15), lineWidth: 1)
                    )
                    .shadow(radius: 6, y: 3)
                    .offset(x: offset.width, y: offset.height)
                    .gesture(
                        DragGesture()
                            .onChanged { value in
                                // follow the finger relative to last saved offset
                                offset = CGSize(width: lastOffset.width + value.translation.width,
                                                height: lastOffset.height + value.translation.height)
                            }
                            .onEnded { _ in
                                lastOffset = offset
                            }
                    )
                    .accessibilityIdentifier("wooden_nail")

                // show a label below the nail so its purpose is obvious
                VStack {
                    Spacer()
                    Text("Drag the wooden nail")
                        .font(.headline)
                        .foregroundColor(.primary)
                        .padding(.bottom, 28)
                        .accessibilityIdentifier("drag_instructions")
                }
            }
            .onAppear {
                // Initialize the nail at the center of the available area (only once)
                if !initialized {
                    // center coordinates (we use 0-based offset from center)
                    let centerX = (geo.size.width / 2) - (geo.size.width / 2)
                    let centerY = (geo.size.height / 2) - (geo.size.height / 2)
                    // center relative to ZStack; we use zero-centered offsets so set offset and lastOffset to zero
                    offset = CGSize(width: 0, height: 0)
                    lastOffset = offset
                    initialized = true
                }
            }
        }
        .navigationTitle("Drag and Drop")
    }
}
