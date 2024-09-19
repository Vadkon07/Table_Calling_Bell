# Table Calling Bell

*An intuitive and engaging table calling solution designed for modern restaurants.*


## Introduction
**Table Calling Bell** is a user-friendly application developed specifically for digitally-forward restaurants aiming to enhance customer service. With a simple interface, guests can easily summon assistance by clicking a charming bell icon, streamlining the dining experience and improving operational efficiency.

> **Note: This app was developed for one very digital restaurant, which soon will be open.**

Additionally, the restaurant owner requested the inclusion of an Easter egg feature that plays a different sound on every 100th click. This unique functionality serves as a subtle advertisement for the restaurant. You have the option to remove or replace this feature if desired.

**Display Optimization:** The app is designed for very small displays, making it perfect for smartphones. It is not optimized for larger screens, so functionality and appearance may be limited on devices bigger than a typical smartphone.

## Features
- **Interactive Bell Interface:** A visually appealing bell that responds to user clicks.
- **Customizable Sound Effects:** Plays a standard call bell sound on each click.
- **Easter Egg Functionality:** Every 100th click triggers a special sound effect, adding a unique touch to the dining experience.
- **Optimized for Small Displays:** Perfectly suited for smartphones and compact screens, ensuring seamless integration into tablet-based ordering systems.

## Installation
### Prerequisites
- **Python 3.7+**
- **Pip** (Python package installer)

### Steps
1. **Clone the repository**
```console
git clone https://github.com/Vadkon07/Table_Calling_Bell.git
cd Table_Calling_Bell/
```
2. **Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```
3. **Install Dependencies**
```console
pip install -r requirements.txt
```
4. **Add Sound and Image Assets**

Ensure that the following files are placed in the project's root directory:

- `bell.wav` – Standard call bell sound.
- `anime-moan.wav` – Easter egg sound effect.
- `bell.jpg` – Image displayed as the clickable bell.

*Alternatively, you can update the paths in the source code to point to your preferred asset locations.*

## Usage
1. **Run the Application**
```console
python .\main.py
```
2. **Interact with the Bell**
- **Standard Usage:** Click the bell image to play the call bell sound, notifying staff for service.
- **Easter Egg:** On every 100th click, a special sound will play as a fun surprise for your guests.


## Customization
### Modifying Sounds
- **Standard Bell Sound:** Replace `bell.wav` with your desired sound file. Ensure the file format is supported (e.g., `.wav` or `.ogg`).
- **Easter Egg Sound:** Replace `anime-moan.wav` with your preferred sound for the Easter egg feature.

### Changing the Bell Image
- Replace `bell.jpg` with another image file of your choice. Ensure the new image maintains a similar aspect ratio for optimal display.

### Adjusting Click Threshold
- To change the number of clicks required to trigger the Easter egg, modify the condition in the `play_sound` method within `main.py`:
```python
if self.clicks > YOUR_DESIRED_THRESHOLD:
    self.moan_sound.play()
    self.clicks = 0
```

### Removing or Replacing the Easter Egg
- If you prefer not to have the Easter egg feature, you can either remove the related code in the `play_sound` method or replace the sound file with another of your choosing.

## To-Do
Here are several ideas to enhance and expand the functionality of the **Table Calling Bell** application:

1. **Add Animations on Click**
- Implement visual feedback such as a brief animation or visual effect when the bell is clicked to enhance user engagement.
2. **User Interface Enhancements**
- Design a more polished and customizable UI, allowing restaurant owners to adjust colors, themes, and layout to match their branding.
3. **Sound Customization Settings**
- Provide an in-app settings menu where users can upload and select their own sound effects for both standard and Easter egg clicks.
4. **Support for Multiple Languages**
- Implement multi-language support to cater to a diverse customer base, making the app accessible to non-English speakers.
5. **Integration with Restaurant Management Systems**
- Enable integration with existing restaurant management or point-of-sale (POS) systems to log service requests and monitor usage statistics.
6. **Responsive Design for Various Screen Sizes**
- Optimize the application layout to support a wider range of devices, including tablets and larger displays, ensuring a consistent user experience across all platforms.
7. **Accessibility Features**
- Incorporate accessibility options such as high-contrast modes, screen reader compatibility, and alternative input methods to ensure the app is usable by all guests.
8. **Analytics and Reporting**
Add functionality to track and report metrics such as total clicks, peak usage times, and Easter egg activations to help restaurant owners gain insights into customer behavior.
9. **Remote Configuration and Updates**
- Allow remote updates and configuration changes, enabling restaurant owners to manage settings without needing direct access to the device running the app.
10. **Battery and Performance Optimization**
- Enhance the app’s performance to minimize battery usage and ensure smooth operation, especially on devices with limited resources.
11. **Multi-User Support**
- Allow multiple users (e.g., different tables) to interact with the app simultaneously, each with individual tracking and notifications.
12. **Push Notifications**
- Implement push notifications to alert staff immediately when a bell is clicked, ensuring prompt service.


## Contributing
We welcome contributions from the community! To contribute:
1. **Fork the Repository**
2. **Create a Feature Branch**
```console
git checkout -b feature/YourFeatureName
```
3. **Commit Your Changes**
```console
git commit -m "Add your message here"
```
4. **Push to the Branch**
```console
git push origin feature/YourFeatureName
```
5. **Open a Pull Request**

Please ensure your code adheres to the project's coding standards and includes appropriate comments and documentation.

## Contact
For any inquiries or support, please contact:

Developer: Vadim Kondratov
Email: vadkonbeats@gmail.com
GitHub: Vadkon07

*Thank you for using Table Calling Bell! We hope it enhances the dining experience at your restaurant.*