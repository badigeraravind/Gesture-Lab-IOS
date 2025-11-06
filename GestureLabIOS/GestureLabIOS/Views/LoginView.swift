import SwiftUI

struct LoginView: View {
    @Binding var navPath: [String]

    @State private var username = ""
    @State private var password = ""
    @State private var error: String?

    var body: some View {
        VStack(spacing: 20) {
            Text("GestureLab")
                .font(.system(size: 28, weight: .bold))

            TextField("Username", text: $username)
                .textFieldStyle(.roundedBorder)
                .accessibilityIdentifier("username_field")

            SecureField("Password", text: $password)
                .textFieldStyle(.roundedBorder)
                .accessibilityIdentifier("password_field")

            Button("Login") {
                attemptLogin()
            }
            .frame(maxWidth: .infinity)
            .buttonStyle(.borderedProminent)
            .accessibilityIdentifier("login_button")

            if let e = error {
                Text(e)
                    .foregroundColor(.red)
                    .accessibilityIdentifier("login_error")
            }
        }
        .padding(24)
        //.accessibilityIdentifier("login_screen")
    }

    private func attemptLogin() {
        error = nil
        if username.trimmingCharacters(in: .whitespaces).isEmpty ||
           password.trimmingCharacters(in: .whitespaces).isEmpty {
            error = "Please enter username and password"
            return
        }
        if username == "falsename" && password == "false@902" {
            error = "invalid username or password"
            return
        }
        // push the "home" value onto the path for NavigationStack to handle
        navPath.append("home")
    }
}
