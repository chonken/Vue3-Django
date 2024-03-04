/**
 * --------------------------------------------------------------------------
 * 事件函數集
 * --------------------------------------------------------------------------
 */

/**
 * 按鈕切換的事件函數
 * @param {object} obj 要切換的按鈕
 * @returns {boolean} 是否執行切換
 */
function switchActive(obj) {
    const oldActiveObj = asideBtns.querySelector('.active');
    if (oldActiveObj && oldActiveObj !== obj){
        oldActiveObj.classList.remove('active');
        obj.classList.add('active');
        return true;
    }
    else{
        return false;
    }
}
/**
 * editAccInfo.html的事件函數:
 * #editName、#denyNewName的按鈕切換事件
 */
function editAccNameEvent() {
    const editName = document.getElementById('editName');
    const inputName = document.getElementById('inputName');
    const confirmNewName = document.getElementById('confirmNewName');
    const denyNewName = document.getElementById('denyNewName');

    editName.addEventListener('click', () => {
        editName.style.display = 'none';
        inputName.style.display = 'block';
        confirmNewName.style.display = 'inline-block';
        denyNewName.style.display = 'inline-block';
    });
    denyNewName.addEventListener('click', () => {
        editName.style.display = 'flex';
        inputName.style.display = 'none';
        confirmNewName.style.display = 'none';
        denyNewName.style.display = 'none';
    });
}
/**
 * maintainCustomerInfo.html的事件函數
 * #denyBtn的取消按鈕事件函數
 */
function maintainCustomerInfoEvent() {
    const main = document.querySelector('main');
    const denyBtn = document.getElementById('denyBtn');
    denyBtn.addEventListener('click', function() {
        axios.get('ajax/maintainCustomerInfo.html')
                .then((response) => main.innerHTML = response.data);
    });
}
/**
 * userPermissions.html的事件函數
 * #navCenter、#navCompany的按鈕事件函數和#selectCompany的下拉式選單系列事件函數
 */
function userPromessionsNavEvent() {
    const navCenter = document.getElementById('navCenter');
    const navCompany = document.getElementById('navCompany');
    const selectCompany = document.querySelector('#selectCompany');
    const dropdownBtn = selectCompany.querySelector('button');
    const dropdownList = selectCompany.querySelectorAll('.dropdown-item');
    const tabCenter = document.getElementById('tabCenter');
    const tabCompany = document.getElementById('tabCompny');
    const activeNav = document.getElementById('activeNav');
    const centerW = navCenter.offsetWidth;
    const companyW = navCompany.offsetWidth;

    navCenter.addEventListener('click', () => {
        navCenter.classList.add('active', 'disabled');
        tabCenter.style.display = 'table';
        navCompany.classList.remove('active', 'disabled');
        tabCompany.style.display = 'none';
        // 導覽底線切換
        activeNav.style.left = '0px';
        activeNav.style.width = centerW + 'px';
    });
    navCompany.addEventListener('click', () => {
        navCompany.classList.add('active', 'disabled');
        tabCompany.style.display = 'table';
        navCenter.classList.remove('active', 'disabled');
        tabCenter.style.display = 'none';
        // 導覽底線切換
        activeNav.style.left = centerW + 'px';
        activeNav.style.width = companyW + 'px';
    });
    changeDropdownText(dropdownBtn);
    dropdownList.forEach((item) => {
        item.addEventListener('click', () => {
            const activeCompany = selectCompany.querySelector('.dropdown-item.active');
            activeCompany.classList.remove('active');
            item.classList.add('active');
            changeDropdownText(dropdownBtn, item.textContent);
        });
    });
}
/**
 * bootstrap下拉式選單的按鈕文字內容為其選中的選項
 * @param {HTMLButtonElement} dropdownBtn 下拉式選單按鈕
 * @param {string | boolean} text 下拉式選單按鈕的文字(選填)
 */
function changeDropdownText(dropdownBtn, text=false){
    if (!text) {
        const temp = document.querySelector('.dropdown-item.active');
        text = temp.textContent || "選擇公司廠別";
    }
    dropdownBtn.innerText = text;
}
/**
 * 提示尚未儲存的函數
 */
// 提示儲存 (尚未實裝)
function notSaved(){
    const modal = new bootstrap.Modal(document.getElementById('saveTip'));
    modal.show();
}