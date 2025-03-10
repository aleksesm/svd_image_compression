from skimage import io
from svd_compression.compression import svd_compression
from svd_compression.visualization import (
    display_image_comparison,
    plot_singular_values,
    plot_rgb_singular_values,
    plot_combined_singular_values
)


def main():
    img_path = "../sample_images/shapes_gray.jpg"
    target_compression_rate = 0.05

    # Compression Options
    compressed_rgb, singular_values_rgb = svd_compression(img_path, target_compression_rate, gray=False)
    compressed_gray, singular_values_gray = svd_compression(img_path, target_compression_rate, gray=True)

    # Visualization Options
    display_image_comparison(io.imread(img_path), compressed_rgb)  # Show side-by-side comparison for RGB
    display_image_comparison(io.imread(img_path), compressed_gray)
    plot_rgb_singular_values(singular_values_rgb, log_scale=False)  # Singular values for RGB channels
    plot_combined_singular_values(singular_values_rgb)  # Combined singular values for RGB channels
    plot_singular_values(singular_values_gray, "Singular Value Decay for Grayscale Image")  # Singular values for grayscale


if __name__ == "__main__":
    main()
