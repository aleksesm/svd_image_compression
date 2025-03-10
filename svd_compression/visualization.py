import matplotlib.pyplot as plt


def plot_singular_values(singular_values, title, log_scale=True):
    """
    Plot singular values with optional logarithmic scale.
    """
    plt.figure(figsize=(8, 4))
    plt.plot(singular_values, linestyle='-', color='k')
    plt.title(title)
    plt.xlabel('Index of Singular Value')
    plt.ylabel('Magnitude')
    if log_scale:
        plt.yscale('log')  # Logarithmic scale
    plt.grid(True)
    plt.show()


def plot_rgb_singular_values(singular_values_rgb, channels=['Red', 'Green', 'Blue'], log_scale=True):
    """
    Plot singular values for RGB channels, ensuring the same y-scale.
    """
    colors = ['r', 'g', 'b']
    fig, ax = plt.subplots(1, 3, figsize=(18, 6))  # 3 subplots in a row

    # Determine the y-axis limits across all singular values
    min_val = min(min(sv) for sv in singular_values_rgb)
    max_val = max(max(sv) for sv in singular_values_rgb)

    for idx, singular_values in enumerate(singular_values_rgb):
        ax[idx].plot(singular_values, linestyle='-', color=colors[idx])
        ax[idx].set_title(f'Singular Value Decay for {channels[idx]} Channel')
        ax[idx].set_xlabel('Index of Singular Value')
        ax[idx].set_ylabel('Magnitude')
        if log_scale:
            ax[idx].set_yscale('log')  # Apply log scale correctly
        ax[idx].set_ylim(min_val, max_val)  # Set the same y-axis scale
        ax[idx].grid(True)

    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()


def plot_combined_singular_values(singular_values_rgb, channels=['Red', 'Green', 'Blue'], log_scale=True):
    """
    Plot singular values of all RGB channels together on one plot.
    """
    plt.figure(figsize=(8, 6))
    colors = ['r', 'g', 'b']

    for idx, singular_values in enumerate(singular_values_rgb):
        plt.plot(singular_values, linestyle='-', color=colors[idx], label=channels[idx])

    plt.title(f'Singular Value Decay for All RGB Channels')
    plt.xlabel('Index of Singular Value')
    plt.ylabel('Magnitude')
    if log_scale:
        plt.yscale('log')  # Logarithmic scale
    plt.legend()
    plt.grid(True)
    plt.show()


def display_image_comparison(original_image, compressed_image):
    """
    Display side-by-side comparison of original and compressed images.
    """
    fig, ax = plt.subplots(1, 2, figsize=(18, 8))  # Increased image size

    # If the images are grayscale (2D) or RGB (3D)
    if compressed_image.ndim == 3:  # RGB to RGB
        ax[0].imshow(original_image)
        ax[1].imshow(compressed_image)
    else:  # RGB to grayscale
        ax[0].imshow(original_image, vmin=0, vmax=255)
        ax[1].imshow(compressed_image, cmap="gray", vmin=0, vmax=255)

    ax[0].set_title("Original Image")
    ax[0].axis('off')
    ax[1].set_title("Compressed Image")
    ax[1].axis('off')

    plt.show()
