import argparse
from compression import svd_compression
from visualization import (display_image_comparison, plot_rgb_singular_values, plot_combined_singular_values,
                           plot_singular_values)


def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Image Compression using SVD")

    # Add arguments for the CLI
    parser.add_argument("image_path", type=str, help="Path to the input image.")
    parser.add_argument("compression_rate", type=float, help="Compression rate (between 0 and 1).")
    parser.add_argument("--grayscale", action="store_true", help="Compress to grayscale instead of RGB.")
    parser.add_argument("--visualize", action="store_true", help="Visualize the results (singular values, images).")
    parser.add_argument("--output", type=str, default=None, help="Path to save the compressed image.")

    # Parse the arguments
    args = parser.parse_args()

    # Perform the compression
    print(f"Compressing {args.image_path} with a compression rate of {args.compression_rate}...")
    compressed_image, singular_values_rgb = svd_compression(args.image_path, args.compression_rate, gray=args.grayscale)

    # Display comparison images if requested
    if args.visualize:
        # Load original image
        from skimage import io
        original_image = io.imread(args.image_path)

        # Display the original and compressed images
        display_image_comparison(original_image, compressed_image)

        # Plot singular values
        if args.grayscale:
            plot_singular_values(singular_values_rgb, title="Singular Value Decay for Grayscale Image")
        else:
            plot_rgb_singular_values(singular_values_rgb)
            plot_combined_singular_values(singular_values_rgb)

    # Save the compressed image if an output path is specified
    if args.output:
        from PIL import Image
        compressed_image_pil = Image.fromarray(compressed_image)
        compressed_image_pil.save(args.output)
        print(f"Compressed image saved to {args.output}")

    print("Compression process completed.")


if __name__ == "__main__":
    main()
