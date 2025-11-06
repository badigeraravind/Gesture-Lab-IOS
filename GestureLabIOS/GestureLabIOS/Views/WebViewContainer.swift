//
//  Untitled 9.swift
//  GestureLabIOS
//
//  Created by Aravind Badiger on 30/10/25.
//

import SwiftUI
import WebKit

struct WebViewContainer: UIViewRepresentable {
    let urlString: String
    func makeUIView(context: Context) -> WKWebView {
        let w = WKWebView()
        w.navigationDelegate = context.coordinator
        w.allowsBackForwardNavigationGestures = true
        if #available(iOS 14.0, *) {
            // Use defaultWebpagePreferences on newer APIs
            w.isInspectable = true
            w.configuration.defaultWebpagePreferences.allowsContentJavaScript = true
        } else {
            w.configuration.preferences.javaScriptEnabled = true
        }
        return w
    }
    func updateUIView(_ uiView: WKWebView, context: Context) {
        if let u = URL(string: urlString) {
            uiView.load(URLRequest(url: u))
        } else {
            uiView.load(URLRequest(url: URL(string: "https://www.google.com")!))
        }
    }
    func makeCoordinator() -> Coordinator { Coordinator() }
    class Coordinator: NSObject, WKNavigationDelegate {
        func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
            webView.load(URLRequest(url: URL(string: "https://www.google.com")!))
        }
    }
}
