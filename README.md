Image Compression using Singular Value Decomposition (SVD)

Overview

This project explores Singular Value Decomposition (SVD) for image compression, inspired by my linear algebra course. I wanted to apply theoretical concepts to a real-world problem and visually understand how SVD affects image data.

The program allows users to compress images using SVD while controlling the compression rate. It supports both RGB and grayscale compression and provides visualization tools to analyze singular value decay.

Features

Compress images using SVD with a specified compression rate.

Supports both grayscale and RGB images.

Visualize singular value decay for each color channel.

Side-by-side comparison of original and compressed images.

Command-Line Interface (CLI) for easy execution.

How It Works

SVD decomposes an image matrix into three matrices:

By keeping only the first k singular values, we approximate the image while significantly reducing its size.

Compression Rate and k Selection

The number of singular values k is calculated based on the target compression rate.

If converting an RGB image to grayscale, we adjust k to maintain an equivalent compression ratio.

Installation

Dependencies

Make sure you have Python installed and install the required packages:

pip install numpy matplotlib scikit-image pillow argparse

Usage

CLI Execution

Run the program using the command line:

python svd_compression/cli.py <image_path> <compression_rate> [--grayscale] [--visualize] [--output <output_path>]

Example Commands

Compress an image to 10% of its original size and visualize the results:

python svd_compression/cli.py sample_images/nature.jpg 0.1 --visualize

Compress an image to grayscale and save the output:

python svd_compression/cli.py sample_images/nature.jpg 0.1 --grayscale --output compressed_nature.jpg

Visualization

If --visualize is enabled, the program generates:

A side-by-side comparison of the original and compressed images.

Singular value decay plots:

Individual plots for Red, Green, and Blue channels.

A combined plot to compare singular values across channels.

Project Structure

svd_compression/
│── cli.py                # CLI interface
│── compression.py        # Core compression logic
│── visualization.py      # Visualization functions
│── sample_images/        # Folder for test images

License

This project is open-source and available under the MIT License.

I hope this project provides insight into the power of SVD in image compression!

