// 容器
const main = document.querySelector('main');
const asideBtns = document.querySelector('.sideBar-body');
// 元件
const editAccInfo_btn = document.getElementById('editAccInfo');
const addCenter_btn =  document.getElementById('addCenter');
const addCompany_btn =  document.getElementById('addCompany');
const maintainCustomerInfo_btn = document.getElementById('maintainCustomerInfo');
const userPormissions_btn = document.getElementById('userPormissions');

// 默認子頁
editAccInfo_btn.classList.add('active');
axios.get('ajax/editAccInfo.html')
    .then((response) => {
        main.innerHTML = response.data
        // 編輯使用者名稱的事件函數
        editAccNameEvent();
    });

// 首頁事件監聽 & 子頁事件監聽
editAccInfo_btn.addEventListener('click', function() {
    // 切換active
    if(switchActive(this)){
        axios.get('ajax/editAccInfo.html')
            .then((response) => {
                main.innerHTML = response.data
                editAccNameEvent();
            });
    }
});
addCenter_btn.addEventListener('click', function() {
    // 切換active
    if(switchActive(this)){
        axios.get('ajax/addCenter.html')
            .then((response) => main.innerHTML = response.data);
    }
});
addCompany_btn.addEventListener('click', function() {
    // 切換active
    if(switchActive(this)){
        axios.get('ajax/addCompany.html')
            .then((response) => main.innerHTML = response.data);
    }
});
maintainCustomerInfo_btn.addEventListener('click', function() {
    // 切換active
    if(switchActive(this)){
        axios.get('ajax/maintainCustomerInfo.html')
            .then((response) => {
                main.innerHTML = response.data
                // 設定使用者權限的事件函數
                maintainCustomerInfoEvent();
            });
    }
});
userPormissions_btn.addEventListener('click', function() {
    // 切換active
    if(switchActive(this)){
        axios.get('ajax/userPormissions.html')
            .then((response) => {
                main.innerHTML = response.data
                // 設定使用者權限的事件函數
                userPremessionsNavEvent();
            });
    }
});