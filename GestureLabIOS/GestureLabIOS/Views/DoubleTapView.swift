import SwiftUI

struct DoubleTapView: View {
    @State private var isSpinning = false

    var body: some View {
        VStack(spacing: 16) {
            Text("Double tap the teddy to start/stop spinning")
                .multilineTextAlignment(.center)

            ZStack {
                // Background box
                RoundedRectangle(cornerRadius: 28)
                    .fill(Color(red: 0.73, green: 0.87, blue: 0.98))
                    .frame(width: 160, height: 160)

                // Teddy that spins
                Text("🐻")
                    .font(.system(size: 64))
                    .rotationEffect(.degrees(isSpinning ? 360 : 0))
                    .animation(
                        isSpinning
                        ? Animation.linear(duration: 1).repeatForever(autoreverses: false)
                        : .default,
                        value: isSpinning
                    )
            }
            // Make the whole rounded area tappable
            .contentShape(RoundedRectangle(cornerRadius: 28))
            // Detect double tap
            .gesture(
                TapGesture(count: 2).onEnded {
                    isSpinning.toggle()
                }
            )
            .accessibilityIdentifier("toy_box")

            Spacer()
        }
        .padding()
        .navigationTitle("Double Tap")
    }
}

struct DoubleTapView_Previews: PreviewProvider {
    static var previews: some View {
        NavigationView {
            DoubleTapView()
        }
    }
}
