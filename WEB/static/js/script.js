const dragArea=document.querySelector('.drag-area')
const dragText = document.querySelector('.header');

let button = document.querySelector('.button');
let input = document.querySelector('input');

let file;
button.onclick = () => {
    input.click();
};

//브라우저 창이 열리면
input.addEventListener('change', function(){
    file = this.files[0];
    dragArea.classList.add('active')
    displayFile();
})
//파일이 드래그 에이리어 안에 있을 때
dragArea.addEventListener('dragover',(event)=>{
    event.preventDefault();
    dragText.textContent = 'Release to upload';
    dragArea.classList.add('active');
   // console.log('file in drag area');
    });

//파일이 드래그 에이리어 밖으로 나갈 때
dragArea.addEventListener('dragleave',() =>{
    dragText.textContent = 'Drag & Drop';
    dragArea.classList.remove('active');

    //console.log('file left the drag area');
} );

//파일이 드래그 에이리어 안에 드롭되었을 때
dragArea.addEventListener('drop',(event)=>{
    event.preventDefault();

    file = event.dataTransfer.files[0];});
    displayFile();

function displayFile() {
    let flieType = file.type;
    let validExtensions = ['video/mp4']
    if (validExtensions.includes(filetype)) {
        let fileReader = new fileReader();
        fileReader.onload = () => {
            let fileURL = fileReader.result;
        //let vidtag = `<img src="${fileURL}" alt="">`; //<- 업로드한 비디오를 재생하는 기능 구현해야 함.  
        };
        fileReader.readAsDataURL(file);
    }else {
        alert('This filetype is not supported!');
        dragArea.classList.remove('active')
    }
    
    //console.log('file dropped in the drag area');


}
   
