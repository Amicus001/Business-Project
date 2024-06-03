function changeImage(action) {
    var imgElement = document.getElementById('backImage');
    if (action === 'over') {
        imgElement.src = imgElement.getAttribute('data-over-src');
    } else if (action === 'out') {
        imgElement.src = imgElement.getAttribute('data-out-src');
    }
}

function showLoadingPage() {
    const form = document.getElementById('upload-form');
    const formData = new FormData(form);
    fetch(form.action, {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (response.ok) {
            window.location.href = '/input/preview/';
        } else {
            alert('파일 업로드에 실패했습니다.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('업로드 중 오류가 발생했습니다');
    });
}


