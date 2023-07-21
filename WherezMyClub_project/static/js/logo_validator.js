document.getElementById('register_form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form submission
  
    const fileInput = document.getElementById('LogoUpload');
    const file = fileInput.files[0];
    const image = new Image();
  
    image.onload = function () {
      const aspectRatio = image.width / image.height;
      if (Math.abs(aspectRatio - 1 / 1) > 0.01) {
        alert('Logo aspect ratio must be 1:1');
        fileInput.value = ''; // Clear the file input to prevent uploading
        document.getElementById('imagePreview').innerHTML = ''; // Clear the image preview
      } else {
        event.target.submit(); // Submit the form if aspect ratio is valid
      }
    };
  
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        image.src = e.target.result;
      };
      reader.readAsDataURL(file);
    }
  });
  
  // Image preview function remains the same as in the previous example
  function displayImagePreview(image) {
    const previewDiv = document.getElementById('imagePreview');
    previewDiv.innerHTML = ''; // Clear previous preview, if any
    const imgElement = document.createElement('img');
    imgElement.src = image.src;
    imgElement.style.maxWidth = '100%';
    imgElement.style.height = 'auto';
    previewDiv.appendChild(imgElement);
  }
  