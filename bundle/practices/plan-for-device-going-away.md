---
type: Practice
title: Plan for the device going away
description: Hardware links drop, so every screen needs an answer and tests run on real devices.
tags: [hardware, mobile, testing]
generated: { by: claude-code/opus-5-5, at: 2026-10-31T14:55:00Z }
sources:
  - id: phone-post
    resource: https://ilya-paskhover.github.io/2019/11/28/phone-apps-that-talk-to-hardware.html
    title: Phone apps that talk to hardware
---

# The practice

1. On every screen, answer one question: what happens when the device goes away right now?[^phone-post]
2. Test on real phones next to real hardware. Simulators lack the radios that matter.[^phone-post]

# Examples

* BLE links drop.[^phone-post]
* WiFi setup has a moment when the phone leaves its usual network to join the gateway.[^phone-post]
* USB depends on the phone, the cable and the permissions dialog.[^phone-post]

# Related

Part of the [Industrial IoT and hardware](../topics/iot-and-hardware.md) topic.

[^phone-post]: [Phone apps that talk to hardware](https://ilya-paskhover.github.io/2019/11/28/phone-apps-that-talk-to-hardware.html)
