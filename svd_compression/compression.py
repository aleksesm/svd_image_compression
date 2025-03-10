import numpy as np
from skimage import io, color
from scipy.linalg import svd


def compute_svd_compression(channel: np.ndarray, k: int) -> np.ndarray:
    """Computes SVD-based compression for a single image channel."""
    U, S, Vt = svd(channel, full_matrices=False)  # Using scipy.linalg.svd
    return U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :], S  # Return singular values as well


def calculate_optimal_k(m, n, target_compression_rate, rgb_to_gray=False):
    """Calculate the optimal number of singular values (k) to achieve the target compression rate."""
    original_size = m * n
    compressed_size = target_compression_rate * original_size
    k = (compressed_size / (m + n + 1))

    if rgb_to_gray:
        k = 3 * k  # Adjust k for RGB to grayscale conversion

    return int(np.floor(k))


def svd_compression(image_path: str, target_compression_rate: float, gray: bool = False):
    """Compresses an image using Singular Value Decomposition (SVD) based on a target compression rate."""
    # Load image
    image = io.imread(image_path)

    # Grayscale compression
    if gray:
        rgb2gray = False
        if image.ndim == 3:  # Convert RGB to grayscale
            image = color.rgb2gray(image)  # Result will be a float32 image in range [0, 1]
            rgb2gray = True
        image = (image * 255).astype(np.uint8)  # Convert to uint8 (range [0, 255])

        m, n = image.shape
        k = calculate_optimal_k(m, n, target_compression_rate, rgb_to_gray=rgb2gray)

        print(f"Retained singular values: {k}")

        # Compute SVD compression
        compressed_gray, singular_values = compute_svd_compression(image.astype(np.float32), k)

        # Normalize & convert back to uint8
        compressed_gray = np.clip(compressed_gray, 0, 255).astype(np.uint8)

        return compressed_gray, singular_values

    # RGB compression
    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("Input image must be an RGB image.")

    m, n, _ = image.shape
    k = calculate_optimal_k(m, n, target_compression_rate)

    print(f"Retained singular values: {k}")

    # Compress each RGB channel separately
    compressed_image = np.zeros_like(image, dtype=np.float32)
    singular_values_rgb = []

    for i in range(3):
        compressed_image[:, :, i], singular_values = compute_svd_compression(image[:, :, i].astype(np.float32), k)
        singular_values_rgb.append(singular_values)

    # Normalize & convert to uint8
    compressed_image = np.clip(compressed_image, 0, 255).astype(np.uint8)

    return compressed_image, singular_values_rgb
