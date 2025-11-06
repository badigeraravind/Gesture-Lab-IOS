//
//  GlobalTouchStore.swift
//  GestureLabIOS
//
//  Created by Aravind Badiger on 30/10/25.
//

import SwiftUI
import Combine
import UIKit

final class GlobalTouchStore: ObservableObject {
    static let shared = GlobalTouchStore()
    @Published var activeTouches: [Int: CGPoint] = [:]

    private init() {}
}

// UIViewRepresentable to capture touches globally and update the store.
struct TouchCaptureView: UIViewRepresentable {
    @EnvironmentObject var store: GlobalTouchStore

    func makeUIView(context: Context) -> TouchCaptureUIView {
        let v = TouchCaptureUIView()
        v.delegate = context.coordinator
        v.isUserInteractionEnabled = true
        v.backgroundColor = .clear
        v.isOpaque = false
        v.translatesAutoresizingMaskIntoConstraints = false
        return v
    }

    func updateUIView(_ uiView: TouchCaptureUIView, context: Context) {
        // nothing
    }

    func makeCoordinator() -> Coordinator {
        Coordinator(store: store)
    }

    class Coordinator: NSObject, TouchCaptureDelegate {
        var store: GlobalTouchStore
        init(store: GlobalTouchStore) { self.store = store }
        func touchesChanged(_ map: [Int: CGPoint]) {
            DispatchQueue.main.async {
                self.store.activeTouches = map
            }
        }
    }
}

// Delegate protocol to pass touches to SwiftUI coordinator
protocol TouchCaptureDelegate: AnyObject {
    func touchesChanged(_ map: [Int: CGPoint])
}

// A UIView subclass that intercepts touch events and forwards them
class TouchCaptureUIView: UIView {
    weak var delegate: TouchCaptureDelegate?

    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) { handleTouches(event) }
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) { handleTouches(event) }
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) { handleTouches(event) }
    override func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?) { handleTouches(event) }

    private func handleTouches(_ event: UIEvent?) {
        var map: [Int: CGPoint] = [:]
        guard let allTouches = event?.allTouches else {
            delegate?.touchesChanged(map)
            return
        }
        for t in allTouches {
            let id = t.hash // stable for that touch object during lifetime
            let point = t.location(in: self)
            map[id] = point
        }
        if allTouches.isEmpty {
            delegate?.touchesChanged([:])
        } else {
            delegate?.touchesChanged(map)
        }
    }
}
