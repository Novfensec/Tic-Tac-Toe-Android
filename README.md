# Tic Tac Toe Android Game

[![Android Build](https://github.com/Novfensec/Tic-Tac-Toe-Android/actions/workflows/buildozer_action.yml/badge.svg)](https://github.com/Novfensec/Tic-Tac-Toe-Android/actions/workflows/buildozer_action.yml)

A classic Tic Tac Toe game developed with Kivy, KivyMD, and KvDeveloper CLI for Android devices. This game showcases advanced Python programming concepts and demonstrates interaction with a neat and intuitive user interface.

<p align="center">
   <img 
      width="800" src="https://raw.githubusercontent.com/Novfensec/Tic-Tac-Toe-Android/main/assets/images/visual.png" style="border-radius:1em" 
      title="Tic-Tac-Toe-Android"
   />
</p>

## Features

- **Clean and Intuitive UI**: Designed with Kivy and KivyMD for a smooth and modern user experience.
- **Advanced Game Logic**: Utilizes advanced Python concepts for game mechanics and logic.
- **Cross-Platform**: Built for Android, but easily adaptable to other platforms.
- **No Dependencies on External Libraries**: Created using the `none` structure in KvDeveloper CLI.

## Table of Contents

- [Installation](#installation)
- [Gameplay](#gameplay)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Novfensec/Tic-Tac-Toe-Android.git
   cd Tic-Tac-Toe-Android
   ```

2. **Build the APK**:
   - The Android build is automated using GitHub Actions with the KvDeveloper CLI command:
     ```bash
     kvdeveloper config-build-setup android --external github
     ```
   - To trigger a build, push to the repository or run the workflow manually via GitHub Actions.
   - Alternatively, the APK can be built on your local development environment using [Buildozer](https://github.com/kivy/buildozer).

3. **Install on Android**:
   - Transfer the APK to your Android device and install it.

## Gameplay

1. Start the game and choose to play as X or O. `(Initially the game starts with X)`
2. Take turns with your opponent until there is a winner or the game ends in a draw.
3. Enjoy the clean UI and smooth game logic!

## Technologies Used

- **Kivy** - Python framework for multi-touch applications
- **KivyMD** - Material Design components for Kivy
- **KvDeveloper CLI** - Command-line interface for managing Kivy/KivyMD projects

## How It Works

The game logic is implemented with efficient Python techniques, making it easy to understand and extend:
- **UI Interactivity**: Built with Kivy's flexible layout options.
- **Advanced Python Concepts**: Ensures robust game logic, handling player turns, win conditions, and draws.
- **No Extra Dependencies**: This project is created using KvDeveloper's `none` structure, focusing on core Kivy and KivyMD features.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/NewFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/NewFeature`).
5. Open a pull request.

## License

This project is open-source and licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
