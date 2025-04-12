# Project StellarX

## Description

StellarX is a platform designed to manage projects within a community/club setting using gamified mechanics. It aims to make project progress visible, encourage participation and peer review, and create an engaging dynamic through a simulated investment market. The ultimate goal is to build a functional, stable platform for approval by HQ.

## Core Features (Based on "The Plan")

1.  **Project Launch System:**
    * Participants log working hours (via Hackatime V2).
    * Projects are represented thematically (e.g., Satellites, Probes).
    * Projects can be launched anytime; continuous work post-launch increases value.
2.  **Voting & Mission Review:**
    * Mandatory peer voting (10 projects) required before launch.
    * Votes include justifications and determine a project's starting multiplier ("thrust").
3.  **Space Investment Market ("Orbital Stock Market"):**
    * Launched projects enter a simulated stock market.
    * Designated "Investors" (HQ members, volunteers) can buy/sell shares using virtual credits.
    * Buying/Selling shares influences the stock price.
    * Logging more hours increases project value/owner credits and potentially stock price.
4.  **Rewards & Investor Returns:**
    * Participants spend earned credits on rewards at the end of an event/cycle.
    * Investors receive a share (e.g., 50%) of their trading profits and get weekly credits to reinvest.

## Key Logic Details (Current Understanding - Needs Final Confirmation)

* **Initial Stock Value:** `Worth per Stock = Hours Worked * Multiplier`
* **Stock Price Change via Trading:** `Buying X shares -> +X% Price Increase`; `Selling Y shares -> -Y% Price Decrease`.
    * **Note:** The exact calculation basis (current price vs. initial price) and the precise mechanism (compounding vs. linear) for the percentage change **needs final clarification with Navdeep**.

## Technology Stack

* **To Be Decided (TBD)**
* Considerations based on team skills/discussion include:
    * Frontend: Framer? Other web technologies?
    * Backend: Python? Node.js?
    * Database: TBD

## Current Status (As of ~April 10-13, 2025)

* **Phase:** Early Development / Planning.
* **Concept:** Core concept ("The Plan") defined.
* **Tasks:** Initial task assignments discussed (Tim: Stocks; Navdeep/Praveen: Main Website - subject to change).
* **Deadline:** A deadline of **April 12th, 2025** was set by Navdeep for project completion and proposal to HQ. Feasibility concerns regarding this deadline have been raised.
* **Roadmap:** Final roadmap needs to be defined (Tim to propose).
* **Logistics:** Communication schedule and other team logistics need to be finalized (Tim to propose).

## Team

* Navdeep
* Timhongphuc
* Praveenkushinpi
