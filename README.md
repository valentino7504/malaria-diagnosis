# Malaria Diagnostic Tool

The Malaria Diagnostic Tool is a web application designed to assist in the detection of malaria using blood smear images. Leveraging a MobileNetV3-based Convolutional Neural Network (CNN), this tool provides an intuitive interface for uploading images and receiving instant diagnostic results.

## Features

- **Image Upload:** Users can upload blood smear images in PNG format.
- **Instant Diagnosis:** The tool processes the uploaded image and provides the likelihood of the sample being "Parasitized" or "Uninfected".
- **User-Friendly Interface:** A simple and clean design makes it easy for users to interact with the application.
- **Probability Display:** The tool shows the probability of each category, enhancing the transparency of the diagnosis.

## Technologies Used

- **Backend:** Flask for serving the application and handling API requests.
- **Machine Learning Model:** MobileNetV3Small-based CNN built with TensorFlow/Keras.
- **Frontend:** HTML, CSS, JavaScript, Tailwind CSS.
- **Deployment:** Render for hosting the backend server.

## Technical Details

### Backend

- **Flask:** The backend is built using Flask, a lightweight WSGI web application framework in Python.
- **Model Loading:** The MobileNetV3-based CNN model is loaded at startup and used for predictions.
- **API Endpoint:** A `/predict` endpoint is provided to handle image uploads and return diagnostic results.

### Frontend

- **HTML/CSS/JavaScript:** The frontend is built with standard web technologies.
- **Tailwind CSS:** Used for styling to ensure a responsive and modern design.
- **Image Upload:** Implements drag-and-drop functionality and standard file input.

## Deployment

The application is deployed on Netlify at [malaria-diagnosis.netlify.app](https://malaria-diagnosis.netlify.app/).

## Contributors

- [Your Name](https://github.com/yourusername)
- [Collaborator Name](https://github.com/collaboratorusername)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact me at [edwinmbonyjr@gmail.com](mailto:edwinmbonyjr@gmail.com) or [edwin.ade@stu.cu.edu.ng](mailto:edwin.ade@stu.cu.edu.ng).
