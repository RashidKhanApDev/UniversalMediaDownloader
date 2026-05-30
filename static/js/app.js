document.addEventListener('DOMContentLoaded', () => {
    const urlInput = document.getElementById('url-input');
    const fetchBtn = document.getElementById('fetch-btn');
    const loader = document.getElementById('loader');
    const loaderText = document.getElementById('loader-text');
    const errorMessage = document.getElementById('error-message');
    const videoCard = document.getElementById('video-card');
    const videoThumbnail = document.getElementById('video-thumbnail');
    const videoTitle = document.getElementById('video-title');
    const formatSelect = document.getElementById('format-select');
    const downloadBtn = document.getElementById('download-btn');

    let currentVideoUrl = '';

    fetchBtn.addEventListener('click', async () => {
        const url = urlInput.value.trim();
        if (!url) {
            showError("Please enter a valid YouTube URL.");
            return;
        }

        currentVideoUrl = url;
        hideError();
        videoCard.classList.add('hidden');
        loaderText.textContent = "Fetching video details...";
        loader.classList.remove('hidden');
        fetchBtn.disabled = true;

        try {
            const response = await fetch('/api/info', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url: url })
            });

            if (!response.ok) {
                const errData = await response.json();
                throw new Error(errData.detail || 'Failed to fetch video info');
            }

            const data = await response.json();
            
            // Populate video card
            videoThumbnail.src = data.thumbnail;
            videoTitle.textContent = data.title;
            
            // Populate formats
            formatSelect.innerHTML = '';
            data.formats.forEach(format => {
                const option = document.createElement('option');
                option.value = format.id;
                option.textContent = format.label;
                formatSelect.appendChild(option);
            });

            loader.classList.add('hidden');
            videoCard.classList.remove('hidden');

        } catch (error) {
            loader.classList.add('hidden');
            showError(error.message);
        } finally {
            fetchBtn.disabled = false;
        }
    });

    downloadBtn.addEventListener('click', async () => {
        const formatId = formatSelect.value;
        if (!formatId || !currentVideoUrl) return;

        hideError();
        downloadBtn.disabled = true;
        
        // Temporarily change button to loading state
        const originalText = downloadBtn.textContent;
        downloadBtn.textContent = 'Processing Download...';
        loaderText.textContent = "Downloading and processing files on server (this may take a while)...";
        loader.classList.remove('hidden');

        try {
            const response = await fetch('/api/download', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    url: currentVideoUrl,
                    format_id: formatId
                })
            });

            if (!response.ok) {
                const errData = await response.json();
                throw new Error(errData.detail || 'Failed to download video');
            }

            const data = await response.json();
            
            // Initiate actual file download in browser
            const downloadUrl = `${data.download_url}?title=${encodeURIComponent(data.title)}`;
            
            // Create a temporary link to download the file
            const a = document.createElement('a');
            a.href = downloadUrl;
            a.download = '';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);

        } catch (error) {
            showError("Download Error: " + error.message);
        } finally {
            downloadBtn.textContent = originalText;
            downloadBtn.disabled = false;
            loader.classList.add('hidden');
        }
    });

    function showError(msg) {
        errorMessage.textContent = msg;
        errorMessage.classList.remove('hidden');
    }

    function hideError() {
        errorMessage.classList.add('hidden');
    }
});
