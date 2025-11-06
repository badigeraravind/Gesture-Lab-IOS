//
//  Untitled 8.swift
//  GestureLabIOS
//
//  Created by Aravind Badiger on 30/10/25.
//

//
//  WebViewLoadingView.swift
//  GestureLabIOS
//
//  Created by Aravind Badiger on 30/10/25.
//

import SwiftUI

struct WebViewLoadingView: View {
    @State private var goToWebview = false

    var body: some View {
        VStack {
            ProgressView().scaleEffect(2)
            Text("Opening WebView…")
            Text("Please wait")
        }
        .onAppear {
            DispatchQueue.main.asyncAfter(deadline: .now() + 7) {
                goToWebview = true
            }
        }
        .background(
            // Use the destination-first initializer and provide the label as a closure
            NavigationLink(destination:
                WebViewContainer(urlString: "https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fbadigeraravind%2Fgame_qa_automation"),
                           isActive: $goToWebview) {
                EmptyView()
            }
        )
        .navigationTitle("Opening Web-View...")
        .accessibilityIdentifier("webview_loading_screen")
    }
}
