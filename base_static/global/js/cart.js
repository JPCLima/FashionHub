// Get elements
const addToCartBts = document.getElementsByClassName('update-cart');

function updateUserOrder(productId, action) {
    const url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action,
        })
    })
    
    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data: ', data)
        location.reload()
    })
    
}

function update_cart(e) {
    const productId = this.dataset.product;
    const action = this.dataset.action;
    console.log('productId: ',productId)
    console.log('action: ',action)
    
    if (user === 'AnonymousUser') {
        console.log('Not logged in')
    }else{
        console.log(`${user} logged in, sending data`);
    const action = this.dataset.action;
        updateUserOrder(productId, action)
    }
}

// Run Code
for (let i = 0; i < addToCartBts.length; i++) {
    addToCartBts[i].addEventListener('click', update_cart);
}
