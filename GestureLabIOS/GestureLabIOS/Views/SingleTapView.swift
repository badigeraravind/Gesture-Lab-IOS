import SwiftUI

struct SingleTapView: View {
    @State private var isOn = false

    var body: some View {
        VStack(spacing: 24) {
            Circle()
                .fill(isOn ? Color.yellow : Color.gray)
                .frame(width: 140, height: 140)
                .overlay(Circle().stroke(Color.gray, lineWidth: 2))
                .accessibilityIdentifier("img_bulb")

            Button(action: { isOn.toggle() }) {
                Text(isOn ? "Switch OFF" : "Switch ON")
                    .frame(maxWidth: .infinity)
            }
            .buttonStyle(.bordered)
            .accessibilityIdentifier(isOn ? "btn_switch_off" : "btn_switch_on")
            Spacer()
        }
        .padding()
        .navigationTitle("Single Tap")
    }
}
