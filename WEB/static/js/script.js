const dragArea = document.querySelector('.drag-drop-area');
const fileInput = document.getElementById('file');
const uploadText = document.getElementById('uploadText');

if (dragArea) {
    dragArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        dragArea.classList.add('drag-over');
    });

    dragArea.addEventListener('dragleave', (e) => {
        e.preventDefault();
        dragArea.classList.remove('drag-over');
    });

    dragArea.addEventListener('drop', (e) => {
        e.preventDefault();
        dragArea.classList.remove('drag-over');
        const files = e.dataTransfer.files;
        handleFiles(files);
        displayFileNames(files);
    });

    dragArea.addEventListener('click', () => {
        fileInput.click();
    });
}

function handleFiles(files) {
    for (const file of files) {
        if (file.type !== 'video/mp4') {
            alert('Only mp4 files can be uploaded');
            return;
        }
    }
}

function displayFileNames(files) {
    let fileNames = [];
    for (const file of files) {
        fileNames.push(file.name);
    }
    if (fileNames.length > 0) {
        uploadText.innerHTML = fileNames.join('<br>');
    } else {
        uploadText.innerHTML = 'Click here or Drag files here to upload videos';
    }
}

fileInput.addEventListener('change', (event) => {
    const files = event.target.files;
    handleFiles(files);
    displayFileNames(files);
});

function dragOverHandler(event) {
    event.preventDefault();
    dragArea.classList.add('drag-over');
}

function startDeIdenfitication() {
    //모델 연결 파트
}