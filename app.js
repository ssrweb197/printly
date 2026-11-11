const products=[
{name:"The Weekly Reset Planner",category:"planner",price:99,description:"A calm, simple layout for priorities, plans and weekly reflection. Includes a weekly overview, top priorities, task list and reflection space."},
{name:"Monthly Money Map",category:"budget",price:149,description:"Track income, expenses, savings goals and monthly spending in one clear printable workbook."},
{name:"Home Reset Checklist",category:"checklist",price:79,description:"A practical home-care checklist covering kitchen, laundry, living spaces and weekly essentials."},
{name:"Small Business Starter Kit",category:"business",price:199,description:"Simple printable trackers for clients, orders, tasks and invoices to help organise a small business."}
];
let active="all";
const cards=[...document.querySelectorAll(".product")], grid=document.getElementById("productGrid"), search=document.getElementById("searchInput"), sort=document.getElementById("sortSelect"), empty=document.getElementById("emptyState");
function applyFilters(){const term=search.value.trim().toLowerCase();let visible=0;let ordered=[...cards];if(sort.value==="low")ordered.sort((a,b)=>+a.dataset.price- +b.dataset.price);if(sort.value==="high")ordered.sort((a,b)=>+b.dataset.price- +a.dataset.price);ordered.forEach(card=>{const match=(active==="all"||card.dataset.category===active)&&card.dataset.name.toLowerCase().includes(term);card.hidden=!match;if(match){visible++;grid.appendChild(card)}});empty.hidden=visible>0}
function setFilter(value){active=value;document.querySelectorAll(".filter").forEach(b=>b.classList.toggle("active",b.dataset.filter===value));applyFilters()}
document.querySelectorAll(".filter").forEach(b=>b.addEventListener("click",()=>setFilter(b.dataset.filter)));
document.querySelectorAll(".category-card").forEach(b=>b.addEventListener("click",()=>{setFilter(b.dataset.filter);document.getElementById("shop").scrollIntoView({behavior:"smooth"})}));
search.addEventListener("input",applyFilters);sort.addEventListener("change",applyFilters);
const modal=document.getElementById("productModal"),title=document.getElementById("modalTitle"),text=document.getElementById("modalText");
function closeModal(){modal.classList.remove("open");modal.setAttribute("aria-hidden","true")}
document.querySelectorAll(".preview-btn").forEach(b=>b.addEventListener("click",()=>{const p=products.find(x=>x.name===b.dataset.product);if(!p)return;title.textContent=p.name;text.textContent=p.description;modal.classList.add("open");modal.setAttribute("aria-hidden","false")}));
document.getElementById("modalClose").addEventListener("click",closeModal);document.getElementById("modalDone").addEventListener("click",closeModal);modal.addEventListener("click",e=>{if(e.target===modal)closeModal()});document.addEventListener("keydown",e=>{if(e.key==="Escape")closeModal()});
document.getElementById("menuBtn").addEventListener("click",()=>document.querySelector(".topbar").classList.toggle("menu-open"));