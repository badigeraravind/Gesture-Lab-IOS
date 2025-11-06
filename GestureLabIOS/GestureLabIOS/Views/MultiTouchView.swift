//
//  Untitled 7.swift
//  GestureLabIOS
//
//  Created by Aravind Badiger on 30/10/25.
//

import SwiftUI

struct MultiTouchView: View {
    // persisted state across gestures
    @State private var baseScale: CGFloat = 1.0
    @State private var baseRotation: Angle = .zero
    @State private var baseOffset: CGSize = .zero

    // transient gesture state (resets per gesture)
    @GestureState private var gestureScale: CGFloat = 1.0
    @GestureState private var gestureRotation: Angle = .zero
    @GestureState private var gestureDrag: CGSize = .zero

    var body: some View {
        VStack {
            Spacer()

            Image("world_map")
                .resizable()
                .scaledToFit()
                .frame(height: 360)
                // apply both persisted and transient transforms
                .scaleEffect(baseScale * gestureScale)
                .rotationEffect(baseRotation + gestureRotation)
                .offset(x: baseOffset.width + gestureDrag.width,
                        y: baseOffset.height + gestureDrag.height)
                // Compose Magnification + Rotation together
                .gesture(
                    SimultaneousGesture(
                        MagnificationGesture()
                            .updating($gestureScale) { latest, state, _ in
                                state = latest
                                #if DEBUG
                                print("[DEBUG] Magnification updating:", latest)
                                #endif
                            }
                            .onEnded { finalValue in
                                baseScale *= finalValue
                                baseScale = min(max(baseScale, 0.4), 6.0)
                                #if DEBUG
                                print("[DEBUG] Magnification ended finalValue:", finalValue, "baseScale:", baseScale)
                                #endif
                            },
                        RotationGesture()
                            .updating($gestureRotation) { latest, state, _ in
                                state = latest
                                #if DEBUG
                                print("[DEBUG] Rotation updating:", latest.degrees)
                                #endif
                            }
                            .onEnded { finalValue in
                                baseRotation += finalValue
                                #if DEBUG
                                print("[DEBUG] Rotation ended finalValue (deg):", finalValue.degrees)
                                #endif
                            }
                    )
                )
                // make drag a high-priority gesture so it doesn't starve magnification
                .highPriorityGesture(
                    DragGesture()
                        .updating($gestureDrag) { latest, state, _ in
                            state = latest.translation
                            #if DEBUG
                            print("[DEBUG] Drag updating:", latest.translation)
                            #endif
                        }
                        .onEnded { finalValue in
                            baseOffset.width += finalValue.translation.width
                            baseOffset.height += finalValue.translation.height
                            #if DEBUG
                            print("[DEBUG] Drag ended:", finalValue.translation)
                            #endif
                        }
                )
                .accessibilityIdentifier("world_map")
                .padding()

            Spacer()

            // small debug display in UI (optional)
            #if DEBUG
            Text(String(format: "Scale: %.2f", baseScale))
                .foregroundColor(.gray)
                .padding(.bottom, 8)
            #endif
        }
        .navigationTitle("Multi-Touch")
    }
}

struct MultiTouchView_Previews: PreviewProvider {
    static var previews: some View {
        MultiTouchView()
    }
}
