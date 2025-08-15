// Mock book data
const mockBooks = [
    {
        id: 1,
        title: "Milk and Honey",
        author: "Rupi Kaur",
        rating: 4.2,
        totalRatings: 874523,
        image: "https://images.unsplash.com/photo-1544947950-fa07a98d237f?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2Nzd8MHwxfHNlYXJjaHwxfHxib29rJTIwY292ZXJzfGVufDB8fHx8MTc1NDE4NTY5NXww&ixlib=rb-4.1.0&q=85",
        description: "A collection of poetry and prose about survival, femininity, and love.",
        pages: 204,
        published: "2014"
    },
    {
        id: 2,
        title: "Your Soul",
        author: "Contemporary Author",
        rating: 4.1,
        totalRatings: 125678,
        image: "https://images.unsplash.com/photo-1511108690759-009324a90311?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2Nzd8MHwxfHNlYXJjaHwyfHxib29rJTIwY292ZXJzfGVufDB8fHx8MTc1NDE4NTY5NXww&ixlib=rb-4.1.0&q=85",
        description: "A deep exploration of self-discovery and spiritual awakening.",
        pages: 312,
        published: "2023"
    },
    {
        id: 3,
        title: "The Subtle Art of Not Giving a F*ck",
        author: "Mark Manson",
        rating: 4.0,
        totalRatings: 456789,
        image: "https://images.unsplash.com/photo-1616687551818-a9218cddd2dc?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2NDF8MHwxfHNlYXJjaHwyfHxiZXN0c2VsbGVyJTIwYm9va3N8ZW58MHx8fHwxNzU0MTkxMTkxfDA&ixlib=rb-4.1.0&q=85",
        description: "A counterintuitive approach to living a good life by caring about fewer things.",
        pages: 224,
        published: "2016"
    },
    {
        id: 4,
        title: "Zero to One",
        author: "Peter Thiel",
        rating: 4.2,
        totalRatings: 234567,
        image: "https://images.unsplash.com/photo-1619872553215-8ac017d003f4?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2NDF8MHwxfHNlYXJjaHwzfHxiZXN0c2VsbGVyJTIwYm9va3N8ZW58MHx8fHwxNzU0MTkxMTkxfDA&ixlib=rb-4.1.0&q=85",
        description: "Notes on startups, or how to build the future by creating something completely new.",
        pages: 210,
        published: "2014"
    },
    {
        id: 5,
        title: "How Innovation Works",
        author: "Matt Ridley",
        rating: 4.3,
        totalRatings: 87654,
        image: "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2Nzd8MHwxfHNlYXJjaHw0fHxib29rJTIwY292ZXJzfGVufDB8fHx8MTc1NDE4NTY5NXww&ixlib=rb-4.1.0&q=85",
        description: "And why it flourishes in freedom - a fascinating look at human innovation.",
        pages: 432,
        published: "2020"
    },
    {
        id: 6,
        title: "Classic Literature",
        author: "Various Authors",
        rating: 4.5,
        totalRatings: 345678,
        image: "https://images.unsplash.com/photo-1592496431122-2349e0fbc666?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2Nzd8MHwxfHNlYXJjaHwzfHxib29rJTIwY292ZXJzfGVufDB8fHx8MTc1NDE4NTY5NXww&ixlib=rb-4.1.0&q=85",
        description: "A collection of timeless stories that have shaped literature.",
        pages: 567,
        published: "Various"
    },
    {
        id: 7,
        title: "Contemporary Fiction",
        author: "Modern Author",
        rating: 3.9,
        totalRatings: 98765,
        image: "https://images.unsplash.com/photo-1556695725-3cc4a29d4ef7?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2NDF8MHwxfHNlYXJjaHwxfHxiZXN0c2VsbGVyJTIwYm9va3N8ZW58MHx8fHwxNzU0MTkxMTkxfDA&ixlib=rb-4.1.0&q=85",
        description: "A modern take on relationships and personal growth.",
        pages: 298,
        published: "2022"
    },
    {
        id: 8,
        title: "Reading Collection",
        author: "Book Enthusiast",
        rating: 4.1,
        totalRatings: 156789,
        image: "https://images.unsplash.com/photo-1664222845171-f9ffe4579c1f?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2NDF8MHwxfHNlYXJjaHw0fHxiZXN0c2VsbGVyJTIwYm9va3N8ZW58MHx8fHwxNzU0MTkxMTkxfDA&ixlib=rb-4.1.0&q=85",
        description: "A curated collection of must-read books for every reader.",
        pages: 145,
        published: "2023"
    }
];

// Application state
let currentUser = null;
let isSignIn = true;
let userShelves = {
    'want-to-read': [],
    'currently-reading': [],
    'read': []
};
let currentShelf = 'want-to-read';
let filteredBooks = [...mockBooks];

// DOM Elements
const authModal = document.getElementById('authModal');
const modalTitle = document.getElementById('modalTitle');
const authForm = document.getElementById('authForm');
const nameGroup = document.getElementById('nameGroup');
const authSubmit = document.getElementById('authSubmit');
const switchBtn = document.getElementById('switchBtn');
const modalClose = document.getElementById('modalClose');
const signInBtn = document.getElementById('signInBtn');
const heroSignUp = document.getElementById('heroSignUp');
const userMenu = document.getElementById('userMenu');
const dropdownMenu = document.getElementById('dropdownMenu');
const searchInput = document.getElementById('searchInput');
const booksGrid = document.getElementById('booksGrid');

// Initialize app
document.addEventListener('DOMContentLoaded', function() {
    // Check for saved user
    const savedUser = localStorage.getItem('goodreads_user');
    const savedShelves = localStorage.getItem('goodreads_shelves');
    
    if (savedUser) {
        currentUser = JSON.parse(savedUser);
        updateUserInterface();
    }
    
    if (savedShelves) {
        userShelves = JSON.parse(savedShelves);
    }
    
    // Render books
    renderBooks();
    
    // Add event listeners
    addEventListeners();
    
    // Initialize My Books page if we're on it
    if (window.location.pathname.includes('my-books.html')) {
        initializeMyBooksPage();
    }
});

// Event listeners
function addEventListeners() {
    // Authentication modal
    if (signInBtn) signInBtn.addEventListener('click', () => showAuthModal());
    if (heroSignUp) heroSignUp.addEventListener('click', () => showAuthModal());
    if (modalClose) modalClose.addEventListener('click', () => hideAuthModal());
    if (switchBtn) switchBtn.addEventListener('click', toggleAuthMode);
    if (authForm) authForm.addEventListener('submit', handleAuth);
    
    // User menu
    if (userMenu) {
        userMenu.addEventListener('click', toggleDropdown);
        const logoutBtn = document.getElementById('logoutBtn');
        if (logoutBtn) logoutBtn.addEventListener('click', handleLogout);
    }
    
    // Search
    if (searchInput) {
        searchInput.addEventListener('input', handleSearch);
    }
    
    // Close modal on overlay click
    if (authModal) {
        authModal.addEventListener('click', (e) => {
            if (e.target === authModal) {
                hideAuthModal();
            }
        });
    }
    
    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
        if (!userMenu?.contains(e.target)) {
            dropdownMenu?.classList.remove('show');
        }
    });
}

// Authentication functions
function showAuthModal() {
    if (authModal) authModal.style.display = 'flex';
}

function hideAuthModal() {
    if (authModal) authModal.style.display = 'none';
}

function toggleAuthMode() {
    isSignIn = !isSignIn;
    
    if (modalTitle) modalTitle.textContent = isSignIn ? 'Sign In' : 'Sign Up';
    if (nameGroup) nameGroup.style.display = isSignIn ? 'none' : 'block';
    if (authSubmit) authSubmit.textContent = isSignIn ? 'Sign In' : 'Sign Up';
    if (switchBtn) {
        switchBtn.textContent = isSignIn ? 
            "Don't have an account? Sign up" : 
            "Already have an account? Sign in";
    }
}

function handleAuth(e) {
    e.preventDefault();
    
    const formData = new FormData(authForm);
    const email = formData.get('email');
    const name = formData.get('name');
    
    currentUser = {
        name: isSignIn ? email.split('@')[0] : name,
        email: email
    };
    
    // Save user to localStorage
    localStorage.setItem('goodreads_user', JSON.stringify(currentUser));
    
    updateUserInterface();
    hideAuthModal();
    
    // Clear form
    authForm.reset();
}

function handleLogout() {
    currentUser = null;
    userShelves = {
        'want-to-read': [],
        'currently-reading': [],
        'read': []
    };
    
    localStorage.removeItem('goodreads_user');
    localStorage.removeItem('goodreads_shelves');
    
    updateUserInterface();
    
    // Redirect to home if on my-books page
    if (window.location.pathname.includes('my-books.html')) {
        window.location.href = 'index.html';
    }
}

function updateUserInterface() {
    const userInitial = document.getElementById('userInitial');
    const userName = document.getElementById('userName');
    const myBooksLink = document.getElementById('my-books-link');
    const readingChallenge = document.getElementById('readingChallenge');
    const welcomeUser = document.getElementById('welcomeUser');
    
    if (currentUser) {
        // Hide sign in button, show user menu
        if (signInBtn) signInBtn.style.display = 'none';
        if (heroSignUp) heroSignUp.style.display = 'none';
        if (userMenu) userMenu.style.display = 'flex';
        if (myBooksLink) myBooksLink.style.display = 'block';
        if (readingChallenge) readingChallenge.style.display = 'block';
        
        // Update user info
        if (userInitial) userInitial.textContent = currentUser.name.charAt(0).toUpperCase();
        if (userName) userName.textContent = currentUser.name;
        if (welcomeUser) welcomeUser.textContent = currentUser.name;
    } else {
        // Show sign in button, hide user menu
        if (signInBtn) signInBtn.style.display = 'block';
        if (heroSignUp) heroSignUp.style.display = 'block';
        if (userMenu) userMenu.style.display = 'none';
        if (myBooksLink) myBooksLink.style.display = 'none';
        if (readingChallenge) readingChallenge.style.display = 'none';
    }
}

function toggleDropdown() {
    if (dropdownMenu) {
        dropdownMenu.classList.toggle('show');
    }
}

// Book functions
function renderBooks() {
    if (!booksGrid) return;
    
    booksGrid.innerHTML = '';
    
    filteredBooks.forEach(book => {
        const bookCard = createBookCard(book);
        booksGrid.appendChild(bookCard);
    });
}

function createBookCard(book) {
    const card = document.createElement('div');
    card.className = 'book-card';
    
    card.innerHTML = `
        <img src="${book.image}" alt="${book.title}" class="book-image">
        <div class="book-info">
            <h3 class="book-title">${book.title}</h3>
            <p class="book-author">by ${book.author}</p>
            <div class="book-rating">
                ${renderStars(book.rating)}
                <span class="rating-text">(${book.totalRatings?.toLocaleString()} ratings)</span>
            </div>
            <p class="book-description">${book.description}</p>
            <div class="book-footer">
                <div class="book-meta">
                    ${book.pages} pages • Published ${book.published}
                </div>
                <div class="want-to-read-container">
                    <button class="want-to-read-btn" onclick="toggleShelfDropdown(${book.id})">
                        Want to Read ▼
                    </button>
                    <div class="shelf-dropdown" id="dropdown-${book.id}">
                        <button class="shelf-option" onclick="addToShelf(${book.id}, 'want-to-read')">Want to Read</button>
                        <button class="shelf-option" onclick="addToShelf(${book.id}, 'currently-reading')">Currently Reading</button>
                        <button class="shelf-option" onclick="addToShelf(${book.id}, 'read')">Read</button>
                    </div>
                </div>
            </div>
        </div>
    `;
    
    return card;
}

function renderStars(rating) {
    const fullStars = Math.floor(rating);
    let starsHtml = '<div class="stars">';
    
    for (let i = 0; i < 5; i++) {
        const filled = i < fullStars;
        starsHtml += `
            <svg class="star ${filled ? 'filled' : 'empty'}" viewBox="0 0 20 20">
                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
            </svg>
        `;
    }
    
    starsHtml += `</div><span>${rating}</span>`;
    return starsHtml;
}

function toggleShelfDropdown(bookId) {
    const dropdown = document.getElementById(`dropdown-${bookId}`);
    const allDropdowns = document.querySelectorAll('.shelf-dropdown');
    
    // Close all other dropdowns
    allDropdowns.forEach(d => {
        if (d.id !== `dropdown-${bookId}`) {
            d.classList.remove('show');
        }
    });
    
    // Toggle current dropdown
    if (dropdown) {
        dropdown.classList.toggle('show');
    }
}

function addToShelf(bookId, shelfType) {
    if (!currentUser) {
        showAuthModal();
        return;
    }
    
    const book = mockBooks.find(b => b.id === bookId);
    if (!book) return;
    
    // Remove book from other shelves
    Object.keys(userShelves).forEach(shelf => {
        userShelves[shelf] = userShelves[shelf].filter(b => b.id !== bookId);
    });
    
    // Add book to specified shelf
    userShelves[shelfType].push(book);
    
    // Save to localStorage
    localStorage.setItem('goodreads_shelves', JSON.stringify(userShelves));
    
    // Close dropdown
    const dropdown = document.getElementById(`dropdown-${bookId}`);
    if (dropdown) dropdown.classList.remove('show');
    
    // Update shelf counts if on my-books page
    updateShelfCounts();
}

function removeFromShelf(bookId, shelfType) {
    userShelves[shelfType] = userShelves[shelfType].filter(b => b.id !== bookId);
    localStorage.setItem('goodreads_shelves', JSON.stringify(userShelves));
    renderShelfBooks();
    updateShelfCounts();
}

function handleSearch() {
    const searchTerm = searchInput.value.toLowerCase();
    
    filteredBooks = mockBooks.filter(book => 
        book.title.toLowerCase().includes(searchTerm) ||
        book.author.toLowerCase().includes(searchTerm)
    );
    
    renderBooks();
}

// My Books page functions
function initializeMyBooksPage() {
    if (!currentUser) {
        window.location.href = 'index.html';
        return;
    }
    
    // Add event listeners for tabs
    const tabBtns = document.querySelectorAll('.tab-btn');
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const shelf = btn.dataset.shelf;
            switchShelf(shelf);
        });
    });
    
    updateShelfCounts();
    renderShelfBooks();
}

function switchShelf(shelf) {
    currentShelf = shelf;
    
    // Update active tab
    const tabBtns = document.querySelectorAll('.tab-btn');
    tabBtns.forEach(btn => {
        btn.classList.toggle('active', btn.dataset.shelf === shelf);
    });
    
    // Update shelf name in empty state
    const shelfName = document.getElementById('shelfName');
    const shelfNames = {
        'want-to-read': 'Want to Read',
        'currently-reading': 'Currently Reading',
        'read': 'Read'
    };
    if (shelfName) shelfName.textContent = shelfNames[shelf];
    
    renderShelfBooks();
}

function updateShelfCounts() {
    const wantCount = document.getElementById('wantCount');
    const currentCount = document.getElementById('currentCount');
    const readCount = document.getElementById('readCount');
    
    if (wantCount) wantCount.textContent = userShelves['want-to-read'].length;
    if (currentCount) currentCount.textContent = userShelves['currently-reading'].length;
    if (readCount) readCount.textContent = userShelves['read'].length;
}

function renderShelfBooks() {
    const shelfBooks = document.getElementById('shelfBooks');
    const emptyShelf = document.getElementById('emptyShelf');
    
    if (!shelfBooks) return;
    
    const books = userShelves[currentShelf] || [];
    
    if (books.length === 0) {
        shelfBooks.innerHTML = '';
        shelfBooks.appendChild(emptyShelf.cloneNode(true));
    } else {
        shelfBooks.innerHTML = '';
        books.forEach(book => {
            const bookCard = createShelfBookCard(book);
            shelfBooks.appendChild(bookCard);
        });
    }
}

function createShelfBookCard(book) {
    const card = document.createElement('div');
    card.className = 'book-card';
    
    card.innerHTML = `
        <img src="${book.image}" alt="${book.title}" class="book-image">
        <div class="book-info">
            <h3 class="book-title">${book.title}</h3>
            <p class="book-author">by ${book.author}</p>
            <div class="book-rating">
                ${renderStars(book.rating)}
            </div>
            <p class="book-description">${book.description}</p>
            <div class="book-footer">
                <div class="book-meta">
                    ${book.pages} pages • Published ${book.published}
                </div>
                <button class="shelf-option" onclick="removeFromShelf(${book.id}, '${currentShelf}')" style="color: #dc2626;">
                    Remove from shelf
                </button>
            </div>
        </div>
    `;
    
    return card;
}

// Close dropdowns when clicking outside
document.addEventListener('click', (e) => {
    if (!e.target.closest('.want-to-read-container')) {
        const dropdowns = document.querySelectorAll('.shelf-dropdown');
        dropdowns.forEach(dropdown => dropdown.classList.remove('show'));
    }
});