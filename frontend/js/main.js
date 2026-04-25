const API_BASE_URL = 'http://localhost:5000/api';
let authToken = localStorage.getItem('authToken');

// API Call Function
async function apiCall(endpoint, method = 'GET', data = null) {
    const headers = {
        'Content-Type': 'application/json',
    };

    if (authToken) {
        headers['Authorization'] = `Bearer ${authToken}`;
    }

    const options = {
        method,
        headers,
    };

    if (data) {
        options.body = JSON.stringify(data);
    }

    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, options);
        const result = await response.json();

        if (!response.ok) {
            if (response.status === 401) {
                localStorage.removeItem('authToken');
                authToken = null;
                showAlert('Session expired. Please login again.', 'error');
            }
            throw new Error(result.error || 'API Error');
        }

        return result;
    } catch (error) {
        console.error('API Error:', error);
        return null;
    }
}

// Show Alert
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;
    alertDiv.style.position = 'fixed';
    alertDiv.style.top = '20px';
    alertDiv.style.right = '20px';
    alertDiv.style.zIndex = '9999';
    alertDiv.style.maxWidth = '400px';

    document.body.appendChild(alertDiv);

    setTimeout(() => {
        alertDiv.remove();
    }, 3000);
}

// Mobile Menu Toggle
const hamburger = document.getElementById('hamburger');
const navMenu = document.querySelector('.nav-menu');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        navMenu.classList.toggle('active');
    });

    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
        });
    });
}

// Authentication
function login(email, password) {
    return apiCall('/auth/login', 'POST', { email, password });
}

function signup(name, email, password, phone) {
    return apiCall('/auth/signup', 'POST', { name, email, password, phone });
}

function getProfile() {
    return apiCall('/auth/profile', 'GET');
}

function updateProfile(name, phone) {
    return apiCall('/auth/profile', 'PUT', { name, phone });
}

function logout() {
    localStorage.removeItem('authToken');
    authToken = null;
    showAlert('Logged out successfully', 'success');
    window.location.href = '/index.html';
}

// Check if user is logged in
function isLoggedIn() {
    return authToken !== null;
}

function requireLogin() {
    if (!isLoggedIn()) {
        showAlert('Please login to continue', 'error');
        window.location.href = '/pages/login.html';
        return false;
    }
    return true;
}

// Format date
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
}

// Format currency
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR'
    }).format(amount);
}

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Initialize on page load
window.addEventListener('load', () => {
    // Update login button based on auth status
    const loginBtn = document.querySelector('.btn-login');
    if (loginBtn && isLoggedIn()) {
        loginBtn.textContent = 'Dashboard';
        loginBtn.href = '/pages/admin.html';
    }
});
