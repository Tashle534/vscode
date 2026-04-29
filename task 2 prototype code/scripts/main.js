
function index(){
    document.querySelector('#redirect')
        .addEventListener('click',()=>{
            window.location.href = "{{ url_for('index') }}"
        })
    
}

function aboutUs(){

    document.querySelector('#redirect')
        .addEventListener('click',()=>{
            window.location.href = "{{url_for('about_us')}}"
        })
    
}
    

function loginPage(){
    document.querySelector('#redirect')

        .addEventListener('click',()=> {
            window.location.href = "{{ url_for('login')}}"

    })
    
}

function SignUP(){
    document.querySelector('#redirect')
        .addEventListener('click',()=> {
            window.location.href = "{{ url_for('sign_up_page')}}"
        })
    
}

function ProductsPage (){
    document.querySelector('#redirect')
        .addEventListener('click',()=> {
            window.location.href = "{{ url_for('products')}}"
        })
    
}

function orderHistory(){
    document.querySelector('#redirect')
        addEventListener('click',()=> {
            window.location.href = "{{ url_for('order_History')}}"
        })
    
}

function checkout(){
    document.querySelector('#redirect')
        addEventListener('click',()=> {
            window.location.href = "{{ url_for('checkout')}}"
        })
    
    
}

function setUpEventListeners(){
    document.getElementById("home").addEventListener("click",index);
    document.getElementById("index").addEventListener("click",index)
    document.getElementById("aboutUs").addEventListener("click",aboutUs)
    document.getElementById("products").addEventListener("click",ProductsPage)
    document.getElementById("login").addEventListener("click",loginPage)
    document.getElementById("signup").addEventListener("click",SignUP)
    document.getElementById("checkout").addEventListener("click",checkout)
    document.getElementById("orderHistory").addEventListener("click",orderHistory)
}