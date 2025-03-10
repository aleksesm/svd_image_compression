# Image Compression using Singular Value Decomposition (SVD)

## Overview

This project explores **Singular Value Decomposition (SVD)** for image compression, inspired by my linear algebra course. I wanted to apply theoretical concepts to a real-world problem and visually understand how SVD affects image data.

The program allows users to compress images using SVD while controlling the compression rate. It supports both **RGB and grayscale** compression and provides visualization tools to analyze singular value decay.

## Features

- **Compress images using SVD** with a specified compression rate.
- **Supports both grayscale and RGB images.**
- **Visualize singular value decay** for each color channel.
- **Side-by-side comparison** of original and compressed images.
- **Command-Line Interface (CLI) for easy execution.**

## How It Works

SVD decomposes an image matrix into three matrices: \(A = U \Sigma V^T\) By keeping only the first **k** singular values, we approximate the image while significantly reducing its size.

### **Compression Rate and k Selection**

- The number of singular values **k** is calculated based on the target compression rate.
- If converting an **RGB image to grayscale**, we adjust k to maintain an equivalent compression ratio.

## Installation

### **Dependencies**

Make sure you have Python installed and install the required packages:

```sh
pip install numpy matplotlib scikit-image pillow argparse
```

## Usage

### **CLI Execution**

Run the program using the command line:

```sh
python svd_compression/cli.py <image_path> <compression_rate> [--grayscale] [--visualize] [--output <output_path>]
```

### **Example Commands**

#### **Compress an image to 10% of its original size and visualize the results:**

```sh
python svd_compression/cli.py sample_images/butterfly.jpg 0.1 --visualize
```

#### **Compress an image to grayscale and save the output:**

```sh
python svd_compression/cli.py sample_images/butterfly.jpg 0.1 --grayscale --output compressed_butterfly.jpg
```

## Visualization

If `--visualize` is enabled, the program generates:

- A **side-by-side comparison** of the original and compressed images.
- **Singular value decay plots**:
  - When compressing RGB to RGB:
      - Individual plots for **Red, Green, and Blue channels**.
      - A combined plot to compare singular values across channels.
  - When compressing RGB to greyscale:
      - A plot for the singular values.

## Project Structure

```
svd_image_compression/ # Root directory of the project
│
├── svd_compression/ # Core module for the SVD compression logic
│   ├── init.py # Initialize the package
│   ├── cli.py # Command-line interface
│   ├── compression.py # Core compression logic
│   └── visualization.py # Visualization functions
│
├── scripts/ # Scripts folder for executable code
│   └── main.py # Main script to execute SVD image compression and display results.
│
├── sample_images/ # Folder containing test images
│
├── requirements.txt # List of dependencies for the project
└── README.md # Project documentation
```

## License

This project is open-source and available under the MIT License.

---

I hope this project provides insight into the power of SVD in image compression!

