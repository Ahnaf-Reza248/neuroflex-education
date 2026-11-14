
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import webbrowser
import threading

PORT = 8000

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Neuroflex Education, an English Medium Institute in Banasree, Dhaka. O Level, A Level, Pre-O Level, PTE and IELTS preparation.">
<title>Neuroflex Education | Inspire Minds. Empower Futures.</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

<style>
:root {
    --navy: #11254b;
    --blue: #3459c8;
    --purple: #7155c7;
    --cyan: #15b8cc;
    --light: #f5f8ff;
    --muted: #68758e;
    --white: #ffffff;
    --border: #e5eaf5;
    --shadow: 0 18px 50px rgba(20, 44, 95, .09);
}

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
    scroll-padding-top: 90px;
}

body {
    margin: 0;
    color: var(--navy);
    background: white;
    font-family: 'DM Sans', Arial, sans-serif;
    line-height: 1.6;
}

h1, h2, h3, h4 {
    font-family: 'Outfit', Arial, sans-serif;
    line-height: 1.15;
    margin-top: 0;
}

a {
    color: inherit;
    text-decoration: none;
}

button, input, select, textarea {
    font: inherit;
}

button {
    cursor: pointer;
}

.container {
    width: min(1160px, 90%);
    margin: auto;
}

.section {
    padding: 95px 0;
}

.section-label {
    color: var(--blue);
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.section-heading {
    font-size: clamp(32px, 4vw, 46px);
    font-weight: 800;
    margin-bottom: 16px;
    letter-spacing: -1.4px;
}

.section-desc {
    color: var(--muted);
    font-size: 16px;
    max-width: 650px;
}

.center {
    text-align: center;
}

.center .section-desc {
    margin: 0 auto;
}

.gradient-text {
    background: linear-gradient(110deg, #3459c8, #7953ce);
    background-clip: text;
    -webkit-background-clip: text;
    color: transparent;
}

.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 9px;
    border: 0;
    border-radius: 12px;
    padding: 14px 23px;
    font-weight: 800;
    font-size: 14px;
    transition: .2s ease;
}

.btn:hover {
    transform: translateY(-3px);
}

.btn-primary {
    color: white;
    background: linear-gradient(120deg, #3158ca, #7658cf);
    box-shadow: 0 8px 25px rgba(54, 83, 202, .22);
}

.btn-outline {
    border: 1.5px solid #a5b2d8;
    color: var(--navy);
    background: white;
}

.btn-white {
    background: white;
    color: var(--blue);
}

/* NAVIGATION */

header {
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(255,255,255,.97);
    border-bottom: 1px solid var(--border);
    backdrop-filter: blur(15px);
}

.navbar {
    min-height: 82px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
}

.logo {
    display: flex;
    align-items: center;
    gap: 12px;
}

.logo-mark {
    width: 49px;
    height: 49px;
    border-radius: 15px;
    background: linear-gradient(145deg, #2e59c8, #8253c6);
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 28px;
    font-weight: 900;
    font-family: 'Outfit';
}

.logo-name {
    font-size: 20px;
    font-weight: 900;
    line-height: 1.05;
    font-family: 'Outfit';
}

.logo-name span {
    display: block;
    color: var(--blue);
}

.logo-tag {
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 1px;
    text-transform: uppercase;
}

.navlinks {
    display: flex;
    align-items: center;
    gap: 27px;
}

.navlinks a:not(.btn) {
    font-size: 14px;
    font-weight: 700;
}

.navlinks a:hover {
    color: var(--blue);
}

.menu-toggle {
    display: none;
    border: 0;
    background: var(--light);
    padding: 9px 14px;
    border-radius: 9px;
    font-size: 23px;
}

/* HERO */

.hero {
    overflow: hidden;
    background:
        radial-gradient(circle at 85% 15%, #d8d9ff 0, transparent 32%),
        linear-gradient(125deg, #f8faff, #edf3ff);
    padding: 90px 0 100px;
}

.hero-grid {
    display: grid;
    grid-template-columns: 1.05fr .95fr;
    align-items: center;
    gap: 55px;
}

.eyebrow {
    display: inline-block;
    background: #e4eaff;
    color: var(--blue);
    padding: 8px 14px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: .7px;
}

.hero h1 {
    font-size: clamp(44px, 5.5vw, 70px);
    letter-spacing: -2.7px;
    margin: 23px 0;
    font-weight: 900;
}

.hero p {
    color: var(--muted);
    max-width: 530px;
    font-size: 17px;
    margin-bottom: 27px;
}

.hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
}

.hero-note {
    margin-top: 30px;
    color: #60708e;
    font-size: 13px;
    font-weight: 700;
}

.hero-visual {
    position: relative;
    min-height: 425px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.visual-circle {
    width: 350px;
    height: 350px;
    border-radius: 50%;
    background: linear-gradient(135deg, #597adf, #7655c8);
    box-shadow: 0 30px 70px rgba(70, 81, 176, .23);
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}

.visual-circle::before {
    content: "";
    position: absolute;
    width: 390px;
    height: 390px;
    border: 2px dashed #b0bce8;
    border-radius: 50%;
}

.book-icon {
    font-size: 132px;
    filter: drop-shadow(0 12px 15px rgba(0,0,0,.15));
}

.floating-card {
    position: absolute;
    background: white;
    border: 1px solid #edf0fa;
    border-radius: 16px;
    padding: 15px 19px;
    box-shadow: var(--shadow);
    z-index: 2;
}

.floating-card strong {
    display: block;
    font-size: 16px;
}

.floating-card small {
    display: block;
    font-size: 12px;
    color: var(--muted);
}

.fc-one {
    top: 35px;
    left: 0;
}

.fc-two {
    right: -5px;
    bottom: 50px;
}

.fc-three {
    left: 20px;
    bottom: 13px;
}

/* FEATURES */

.features {
    margin-top: -48px;
    position: relative;
    z-index: 3;
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.feature {
    padding: 26px;
    background: white;
    border: 1px solid var(--border);
    border-radius: 19px;
    box-shadow: var(--shadow);
}

.feature-icon {
    width: 51px;
    height: 51px;
    background: #e9efff;
    color: var(--blue);
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 27px;
    margin-bottom: 16px;
}

.feature h3 {
    font-size: 20px;
    margin-bottom: 7px;
}

.feature p {
    font-size: 14px;
    color: var(--muted);
    margin: 0;
}

/* SUBJECTS */

.subjects-section {
    background: var(--light);
}

.subjects-grid {
    margin-top: 38px;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
}

.subject-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 23px 16px;
    display: flex;
    align-items: center;
    gap: 12px;
    font-weight: 800;
    transition: .2s;
}

.subject-card:hover {
    border-color: #9aacfc;
    transform: translateY(-4px);
    box-shadow: var(--shadow);
}

.subject-icon {
    font-size: 25px;
}

.subject-card span:last-child {
    font-size: 14px;
}

/* COURSES */

.courses-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
    margin-top: 39px;
}

.course-card {
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 30px;
    transition: .2s;
    background: white;
}

.course-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow);
}

.course-badge {
    width: 62px;
    height: 62px;
    border-radius: 17px;
    background: linear-gradient(130deg, #e4eaff, #f0eaff);
    display: grid;
    place-items: center;
    font-size: 31px;
    margin-bottom: 22px;
}

.course-card h3 {
    font-size: 24px;
    margin-bottom: 10px;
}

.course-card p {
    font-size: 14px;
    color: var(--muted);
    min-height: 70px;
}

.course-card a {
    color: var(--blue);
    font-weight: 800;
    font-size: 14px;
}

.curriculum {
    margin-top: 30px;
    padding: 20px 25px;
    background: #f3f6ff;
    border-radius: 14px;
    text-align: center;
    font-size: 15px;
}

/* WHY CHOOSE */

.why-section {
    background: #f7f9ff;
}

.why-grid {
    display: grid;
    grid-template-columns: .85fr 1.15fr;
    gap: 60px;
    align-items: center;
}

.why-art {
    min-height: 390px;
    background: linear-gradient(145deg, #355ccc, #7d53c5);
    border-radius: 29px;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 35px;
}

.why-art .big-icon {
    font-size: 105px;
    margin-bottom: 15px;
}

.why-art h3 {
    font-size: 33px;
    margin: 0 0 10px;
}

.why-art p {
    max-width: 300px;
    color: #e5eaff;
}

.why-list {
    display: grid;
    gap: 21px;
    margin-top: 25px;
}

.why-item {
    display: flex;
    align-items: flex-start;
    gap: 15px;
}

.check {
    background: #e5edff;
    color: var(--blue);
    border-radius: 10px;
    width: 37px;
    height: 37px;
    display: grid;
    place-items: center;
    font-size: 18px;
    font-weight: 900;
    flex-shrink: 0;
}

.why-item h3 {
    font-size: 18px;
    margin-bottom: 5px;
}

.why-item p {
    color: var(--muted);
    font-size: 14px;
    margin: 0;
}

/* ADMISSION */

.admission {
    padding: 85px 0;
    background: linear-gradient(115deg, #244bbd, #7550bb);
    color: white;
}

.admission-grid {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 40px;
    align-items: center;
}

.admission h2 {
    font-size: clamp(32px, 4vw, 45px);
    margin-bottom: 10px;
}

.admission p {
    color: #e3e9ff;
    margin: 0;
}

.admission .offer {
    display: inline-block;
    margin-top: 15px;
    background: rgba(255,255,255,.15);
    border: 1px solid rgba(255,255,255,.3);
    padding: 8px 13px;
    border-radius: 8px;
    font-size: 13px;
}

/* FORM */

.trial-section {
    background: #f8faff;
}

.trial-grid {
    display: grid;
    grid-template-columns: .85fr 1.15fr;
    gap: 65px;
    align-items: start;
}

.trial-info {
    padding-top: 28px;
}

.trial-points {
    margin-top: 30px;
    display: grid;
    gap: 16px;
}

.trial-point {
    display: flex;
    gap: 12px;
    align-items: center;
    font-weight: 700;
    font-size: 14px;
}

.trial-point span {
    color: var(--blue);
    font-size: 22px;
}

.form-card {
    padding: 35px;
    border-radius: 22px;
    background: white;
    box-shadow: var(--shadow);
    border: 1px solid var(--border);
}

.form-card h3 {
    font-size: 25px;
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 17px;
}

.form-group label {
    display: block;
    font-weight: 800;
    font-size: 13px;
    margin-bottom: 7px;
}

.form-group input,
.form-group select,
.form-group textarea {
    display: block;
    width: 100%;
    border: 1px solid #d9e0ee;
    border-radius: 10px;
    padding: 12px 14px;
    background: #fbfcff;
    color: var(--navy);
    outline: none;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    border-color: var(--blue);
    box-shadow: 0 0 0 3px #e8edff;
}

.form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
}

.form-card .btn {
    width: 100%;
}

.form-notice {
    color: var(--muted);
    font-size: 12px;
    margin-top: 13px;
    text-align: center;
}

#formMessage {
    display: none;
    margin-top: 15px;
    background: #edf8f4;
    color: #23634b;
    border-radius: 10px;
    padding: 12px;
    font-size: 13px;
}

/* CONTACT */

.contact-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
    margin-top: 38px;
}

.contact-card {
    padding: 27px;
    border: 1px solid var(--border);
    border-radius: 18px;
    background: white;
}

.contact-card .contact-icon {
    font-size: 31px;
    margin-bottom: 15px;
}

.contact-card h3 {
    font-size: 20px;
    margin-bottom: 9px;
}

.contact-card p {
    color: var(--muted);
    font-size: 14px;
    margin-bottom: 15px;
    overflow-wrap: anywhere;
}

.contact-card a {
    color: var(--blue);
    font-size: 14px;
    font-weight: 800;
}

/* FOOTER */

footer {
    color: #d1daec;
    background: #101f40;
    padding: 60px 0 25px;
}

.footer-grid {
    display: grid;
    grid-template-columns: 1.4fr 1fr 1fr;
    gap: 50px;
}

.footer-brand h3 {
    color: white;
    font-size: 26px;
    margin-bottom: 10px;
}

.footer-brand p {
    font-size: 14px;
    max-width: 320px;
}

.footer-col h4 {
    color: white;
    margin-bottom: 17px;
    font-size: 17px;
}

.footer-col a {
    display: block;
    margin-bottom: 10px;
    font-size: 14px;
}

.footer-col a:hover {
    color: white;
}

.footer-bottom {
    border-top: 1px solid #31405b;
    padding-top: 22px;
    margin-top: 42px;
    text-align: center;
    font-size: 12px;
}

/* RESPONSIVE */

@media (max-width: 950px) {
    .hero-grid,
    .why-grid,
    .trial-grid {
        grid-template-columns: 1fr;
    }

    .hero-visual {
        min-height: 400px;
    }

    .subjects-grid {
        grid-template-columns: repeat(3, 1fr);
    }

    .courses-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .navlinks {
        gap: 15px;
    }

    .navlinks a {
        font-size: 12px !important;
    }
}

@media (max-width: 700px) {
    .section {
        padding: 65px 0;
    }

    .navbar {
        min-height: 72px;
    }

    .logo-name {
        font-size: 17px;
    }

    .menu-toggle {
        display: block;
    }

    .navlinks {
        display: none;
        position: absolute;
        top: 72px;
        left: 0;
        right: 0;
        padding: 23px 6%;
        background: white;
        border-bottom: 1px solid var(--border);
        flex-direction: column;
        align-items: stretch;
        gap: 19px;
        box-shadow: var(--shadow);
    }

    .navlinks.active {
        display: flex;
    }

    .navlinks a {
        font-size: 15px !important;
    }

    .hero {
        padding: 68px 0 90px;
    }

    .hero h1 {
        font-size: 45px;
    }

    .hero-visual {
        min-height: 340px;
    }

    .visual-circle {
        width: 250px;
        height: 250px;
    }

    .visual-circle::before {
        width: 278px;
        height: 278px;
    }

    .book-icon {
        font-size: 95px;
    }

    .floating-card {
        padding: 10px 12px;
    }

    .floating-card strong {
        font-size: 12px;
    }

    .floating-card small {
        font-size: 10px;
    }

    .fc-one {
        top: 8px;
    }

    .fc-two {
        right: 0;
        bottom: 16px;
    }

    .fc-three {
        left: 2px;
        bottom: 0;
    }

    .feature-grid,
    .contact-grid,
    .footer-grid {
        grid-template-columns: 1fr;
    }

    .subjects-grid,
    .courses-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .admission-grid {
        grid-template-columns: 1fr;
    }

    .form-row {
        grid-template-columns: 1fr;
        gap: 0;
    }

    .form-card {
        padding: 25px;
    }

    .footer-grid {
        gap: 25px;
    }
}

@media (max-width: 420px) {
    .subjects-grid,
    .courses-grid {
        grid-template-columns: 1fr;
    }

    .hero h1 {
        font-size: 39px;
    }
}

@media (prefers-reduced-motion: reduce) {
    html {
        scroll-behavior: auto;
    }

    *, *::before, *::after {
        transition: none !important;
    }
}
</style>
</head>

<body>

<!-- NAVIGATION -->

<header>
    <nav class="navbar container">
        <a href="#home" class="logo" aria-label="Neuroflex Education Home">
            <div class="logo-mark">N</div>
            <div>
                <div class="logo-name">NEUROFLEX <span>EDUCATION</span></div>
                <div class="logo-tag">Inspire Minds. Empower Futures.</div>
            </div>
        </a>

        <button class="menu-toggle" id="menuToggle"
                aria-label="Toggle menu" aria-expanded="false"
                aria-controls="navlinks">☰</button>

        <div class="navlinks" id="navlinks">
            <a href="#home">Home</a>
            <a href="#about">About Us</a>
            <a href="#subjects">Subjects</a>
            <a href="#courses">Courses</a>
            <a href="#contact">Contact</a>
            <a href="#trial" class="btn btn-primary">Free Trial Class ↗</a>
        </div>
    </nav>
</header>

<main>

<!-- HERO SECTION -->

<section class="hero" id="home">
    <div class="container hero-grid">
        <div class="hero-content">
            <span class="eyebrow">✦ AN ENGLISH MEDIUM INSTITUTE</span>

            <h1>
                Inspire Minds.<br>
                <span class="gradient-text">Empower Futures.</span>
            </h1>

            <p>
                Welcome to Neuroflex Education, where we support
                students in building strong academic foundations
                through focused lessons, experienced teachers,
                and a supportive learning environment.
            </p>

            <div class="hero-actions">
                <a href="#trial" class="btn btn-primary">
                    Get 2 Free Trial Classes ↗
                </a>
                <a href="#courses" class="btn btn-outline">
                    Explore Our Courses
                </a>
            </div>

            <div class="hero-note">
                ✓ Admissions Open &nbsp; ✓ English Medium Curriculum
            </div>
        </div>

        <div class="hero-visual">
            <div class="visual-circle">
                <div class="book-icon" role="img" aria-label="Books">📚</div>
            </div>

            <div class="floating-card fc-one">
                <strong>🎓 Expert Teachers</strong>
                <small>Professional educators</small>
            </div>

            <div class="floating-card fc-two">
                <strong>⭐ O Level & A Level</strong>
                <small>Academic preparation</small>
            </div>

            <div class="floating-card fc-three">
                <strong>✓ Supportive Learning</strong>
                <small>Focused lessons</small>
            </div>
        </div>
    </div>
</section>

<!-- FEATURES -->

<div class="features" id="about">
    <div class="container feature-grid">

        <div class="feature">
            <div class="feature-icon">👩‍🏫</div>
            <h3>Expert Teachers</h3>
            <p>
                Learn from dedicated educators with English Medium
                backgrounds and strong curriculum knowledge.
            </p>
        </div>

        <div class="feature">
            <div class="feature-icon">🏫</div>
            <h3>Modern Facilities</h3>
            <p>
                A learning space designed to support concentration,
                participation, and academic development.
            </p>
        </div>

        <div class="feature">
            <div class="feature-icon">🚀</div>
            <h3>Student Activities</h3>
            <p>
                Engaging academic activities and a supportive
                environment to encourage student growth.
            </p>
        </div>

    </div>
</div>

<!-- SUBJECTS -->

<section class="section subjects-section" id="subjects">
    <div class="container">

        <div class="center">
            <div class="section-label">WHAT WE TEACH</div>
            <h2 class="section-heading">
                Explore Our <span class="gradient-text">Subjects</span>
            </h2>
            <p class="section-desc">
                Discover our range of English Medium subjects
                covering science, mathematics, technology,
                languages, and commerce.
            </p>
        </div>

        <div class="subjects-grid">

            <div class="subject-card">
                <span class="subject-icon">📖</span>
                <span>English</span>
            </div>

            <div class="subject-card">
                <span class="subject-icon">⚛️</span>
                <span>Physics</span>
            </div>

            <div class="subject-card">
                <span class="subject-icon">🧪</span>
                <span>Chemistry</span>
            </div>

            <div class="subject-card">
                <span class="subject-icon">🧬</span>
                <span>Biology</span>
            </div>

            <div class="subject-card">
                <span class="subject-icon">📐</span>
                <span>Add / Pure Math</span>
            </div>

            <div class="subject-card">
                <span class="subject-icon">🔢</span>
                <span>Math-B / Math-D</span>
            </div>

            <div class="subject-card">
                <span class="subject-icon">💻</span>
                <span>CS / ICT / IT</span>
            </div>

            <div class="subject-card">
                <span class="subject-icon">💼</span>
                <span>Business</span>
            </div>

            <div class="subject-card">
                <span class="subject-icon">📊</span>
                <span>Economics</span>
            </div>

            <div class="subject-card">
                <span class="subject-icon">🧮</span>
                <span>Accounting</span>
            </div>

            <div class="subject-card">
                <span class="subject-icon">🇧🇩</span>
                <span>Bangla</span>
            </div>

            <div class="subject-card">
                <span class="subject-icon">🫀</span>
                <span>Human Biology</span>
            </div>

        </div>
    </div>
</section>

<!-- COURSES -->

<section class="section" id="courses">
    <div class="container">

        <div class="center">
            <div class="section-label">OUR PROGRAMS</div>
            <h2 class="section-heading">
                Courses for Every <span class="gradient-text">Learning Goal</span>
            </h2>
            <p class="section-desc">
                From early academic preparation to international
                qualifications and English language tests,
                explore the programs offered at Neuroflex Education.
            </p>
        </div>

        <div class="courses-grid">

            <div class="course-card">
                <div class="course-badge">🌱</div>
                <h3>Pre-O Level</h3>
                <p>
                    Foundation preparation to help students develop
                    subject knowledge before entering O Level.
                </p>
                <a href="#trial" data-course="Pre-O Level">
                    Enquire Now →
                </a>
            </div>

            <div class="course-card">
                <div class="course-badge">📘</div>
                <h3>O Level</h3>
                <p>
                    Subject-focused academic preparation aligned
                    with English Medium O Level studies.
                </p>
                <a href="#trial" data-course="O Level">
                    Enquire Now →
                </a>
            </div>

            <div class="course-card">
                <div class="course-badge">🎓</div>
                <h3>A Level</h3>
                <p>
                    Advanced subject preparation to support
                    students working towards A Level qualifications.
                </p>
                <a href="#trial" data-course="A Level">
                    Enquire Now →
                </a>
            </div>

            <div class="course-card">
                <div class="course-badge">🌍</div>
                <h3>PTE</h3>
                <p>
                    English language test preparation for students
                    planning international education opportunities.
                </p>
                <a href="#trial" data-course="PTE">
                    Enquire Now →
                </a>
            </div>

            <div class="course-card">
                <div class="course-badge">🗣️</div>
                <h3>Online IELTS</h3>
                <p>
                    Online preparation for IELTS covering English
                    language skills and examination practice.
                </p>
                <a href="#trial" data-course="Online IELTS">
                    Enquire Now →
                </a>
            </div>

            <div class="course-card">
                <div class="course-badge">🤝</div>
                <h3>Need Guidance?</h3>
                <p>
                    Not sure which course or subject is right
                    for you? Contact our team for information.
                </p>
                <a href="#contact">
                    Contact Us →
                </a>
            </div>

        </div>

        <div class="curriculum">
            <strong>Academic Curricula:</strong>
            Cambridge International Education and
            Pearson Edexcel
        </div>

    </div>
</section>

<!-- WHY CHOOSE US -->

<section class="section why-section" id="why">
    <div class="container why-grid">

        <div class="why-art">
            <div class="big-icon">🎓</div>
            <h3>Learn. Grow. Excel.</h3>
            <p>
                Focused education and guidance
                to help students work towards
                their academic goals.
            </p>
        </div>

        <div class="why-content">
            <div class="section-label">THE NEUROFLEX DIFFERENCE</div>

            <h2 class="section-heading">
                Why Choose
                <span class="gradient-text">Neuroflex Education?</span>
            </h2>

            <p class="section-desc">
                Our approach combines experienced educators,
                focused instruction, and a learning environment
                that encourages student progress.
            </p>

            <div class="why-list">

                <div class="why-item">
                    <div class="check">✓</div>
                    <div>
                        <h3>Senior Mentors</h3>
                        <p>
                            Guidance from experienced teachers
                            with classroom teaching expertise.
                        </p>
                    </div>
                </div>

                <div class="why-item">
                    <div class="check">✓</div>
                    <div>
                        <h3>English Medium Core</h3>
                        <p>
                            Instruction designed around English
                            Medium school standards and curriculum.
                        </p>
                    </div>
                </div>

                <div class="why-item">
                    <div class="check">✓</div>
                    <div>
                        <h3>Professional Educators</h3>
                        <p>
                            Dedicated career teachers with
                            experience delivering classroom lessons.
                        </p>
                    </div>
                </div>

                <div class="why-item">
                    <div class="check">✓</div>
                    <div>
                        <h3>Supportive Learning Environment</h3>
                        <p>
                            A positive environment that encourages
                            participation, confidence and learning.
                        </p>
                    </div>
                </div>

                <div class="why-item">
                    <div class="check">✓</div>
                    <div>
                        <h3>Focused, Effective Lessons</h3>
                        <p>
                            Subject-specific teaching intended to
                            improve understanding and academic readiness.
                        </p>
                    </div>
                </div>

            </div>
        </div>
    </div>
</section>

<!-- ADMISSION -->

<section class="admission" id="admission">
    <div class="container admission-grid">
        <div>
            <div style="font-size:13px;font-weight:800;letter-spacing:2px;">
                YOUR LEARNING JOURNEY STARTS HERE
            </div>

            <h2>Admissions Are Now Open!</h2>

            <p>
                Take the next step towards your academic goals
                with Neuroflex Education.
            </p>

            <div class="offer">
                🎁 Bring the original leaflet to avail available offers.
            </div>
        </div>

        <a href="#trial" class="btn btn-white">
            Register for Free Trial ↗
        </a>
    </div>
</section>

<!-- FREE TRIAL -->

<section class="section trial-section" id="trial">
    <div class="container trial-grid">

        <div class="trial-info">
            <div class="section-label">GET STARTED FOR FREE</div>

            <h2 class="section-heading">
                Sign Up for
                <span class="gradient-text">2 Free Trial Classes!</span>
            </h2>

            <p class="section-desc">
                Interested in studying with us?
                Request information about your two free trial classes.
                Complete the form and send the enquiry through
                your email application.
            </p>

            <div class="trial-points">
                <div class="trial-point">
                    <span>✓</span>
                    Experience our teaching approach.
                </div>

                <div class="trial-point">
                    <span>✓</span>
                    Learn more about your preferred subjects.
                </div>

                <div class="trial-point">
                    <span>✓</span>
                    Explore the learning environment.
                </div>

                <div class="trial-point">
                    <span>✓</span>
                    Discuss course options with the institute.
                </div>
            </div>
        </div>

        <div class="form-card">
            <h3>Request Your Free Trial</h3>

            <form id="trialForm">

                <div class="form-row">
                    <div class="form-group">
                        <label for="studentName">Student Name *</label>
                        <input id="studentName" name="studentName"
                               type="text" placeholder="Full name"
                               autocomplete="name" maxlength="100" required>
                    </div>

                    <div class="form-group">
                        <label for="phone">Contact Number *</label>
                        <input id="phone" name="phone"
                               type="tel" placeholder="+880..."
                               autocomplete="tel" maxlength="30" required>
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="course">Select Course *</label>
                        <select id="course" name="course" required>
                            <option value="">Choose a course</option>
                            <option>Pre-O Level</option>
                            <option>O Level</option>
                            <option>A Level</option>
                            <option>PTE</option>
                            <option>Online IELTS</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="subject">Preferred Subject</label>
                        <select id="subject" name="subject">
                            <option value="">Select a subject</option>
                            <option>English</option>
                            <option>Physics</option>
                            <option>Chemistry</option>
                            <option>Biology</option>
                            <option>Add / Pure Math</option>
                            <option>Math-B / Math-D</option>
                            <option>CS / ICT / IT</option>
                            <option>Business</option>
                            <option>Economics</option>
                            <option>Accounting</option>
                            <option>Bangla</option>
                            <option>Human Biology</option>
                        </select>
                    </div>
                </div>

                <div class="form-group">
                    <label for="email">Email Address *</label>
                    <input id="email" name="email" type="email"
                           placeholder="you@example.com"
                           autocomplete="email" maxlength="254" required>
                </div>

                <div class="form-group">
                    <label for="message">Additional Information</label>
                    <textarea id="message" name="message"
                              rows="4" maxlength="1000"
                              placeholder="Tell us about your learning needs..."></textarea>
                </div>

                <button class="btn btn-primary" type="submit">
                    Prepare Trial Class Enquiry ↗
                </button>

                <div id="formMessage" role="status"></div>

                <p class="form-notice">
                    Submitting opens your email application.
                    You must send the prepared email to complete your enquiry.
                    No information is stored on this website.
                </p>

            </form>
        </div>
    </div>
</section>

<!-- CONTACT -->

<section class="section" id="contact">
    <div class="container">

        <div class="center">
            <div class="section-label">GET IN TOUCH</div>
            <h2 class="section-heading">
                Contact <span class="gradient-text">Neuroflex Education</span>
            </h2>
            <p class="section-desc">
                Have questions about admissions, courses, or trial classes?
                Contact us or visit our institute in Banasree, Dhaka.
            </p>
        </div>

        <div class="contact-grid">

            <div class="contact-card">
                <div class="contact-icon">📞</div>
                <h3>Call Us</h3>
                <p>Speak with our team for admission and course enquiries.</p>
                <a href="tel:+8801845440528">
                    +880 1845-440528 →
                </a>
            </div>

            <div class="contact-card">
                <div class="contact-icon">✉️</div>
                <h3>Email Us</h3>
                <p>Send us your questions about classes and enrollment.</p>
                <a href="mailto:neuroflexed@gmail.com">
                    neuroflexed@gmail.com →
                </a>
            </div>

            <div class="contact-card">
                <div class="contact-icon">📍</div>
                <h3>Visit Our Institute</h3>
                <p>
                    Ground Floor, House-15, Road-3,
                    Block-B, Banasree, Dhaka-1219,
                    Bangladesh.
                </p>

                <a href="https://www.google.com/maps/search/?api=1&query=Neuroflex+Education+Banasree+Dhaka"
                   target="_blank" rel="noopener noreferrer">
                    View on Google Maps →
                </a>
            </div>

        </div>
    </div>
</section>

</main>

<!-- FOOTER -->

<footer>
    <div class="container">

        <div class="footer-grid">
            <div class="footer-brand">
                <h3>NEUROFLEX EDUCATION</h3>
                <p>
                    Inspire Minds. Empower Futures.
                </p>
                <p>
                    An English Medium Institute in Banasree,
                    Dhaka, offering academic and English
                    language test preparation.
                </p>
            </div>

            <div class="footer-col">
                <h4>Quick Links</h4>
                <a href="#home">Home</a>
                <a href="#about">About Us</a>
                <a href="#subjects">Subjects</a>
                <a href="#courses">Courses</a>
                <a href="#trial">Free Trial Classes</a>
            </div>

            <div class="footer-col">
                <h4>Follow Us</h4>

                <a href="https://www.facebook.com/neuroflexed"
                   target="_blank" rel="noopener noreferrer">
                    Facebook ↗
                </a>

                <a href="https://www.instagram.com/neuroflexed"
                   target="_blank" rel="noopener noreferrer">
                    Instagram ↗
                </a>

                <a href="mailto:neuroflexed@gmail.com">
                    Email Us ↗
                </a>

                <a href="tel:+8801845440528">
                    Call Us ↗
                </a>
            </div>
        </div>

        <div class="footer-bottom">
            © <span id="year"></span> Neuroflex Education.
            All Rights Reserved.
        </div>

    </div>
</footer>

<script>
// CURRENT YEAR
document.getElementById("year").textContent = new Date().getFullYear();

// MOBILE NAVIGATION
const menuToggle = document.getElementById("menuToggle");
const navlinks = document.getElementById("navlinks");

menuToggle.addEventListener("click", function () {
    const opened = navlinks.classList.toggle("active");
    menuToggle.setAttribute("aria-expanded", String(opened));
    menuToggle.textContent = opened ? "✕" : "☰";
});

document.querySelectorAll(".navlinks a").forEach(function (link) {
    link.addEventListener("click", function () {
        navlinks.classList.remove("active");
        menuToggle.setAttribute("aria-expanded", "false");
        menuToggle.textContent = "☰";
    });
});

// AUTOMATIC COURSE SELECTION
document.querySelectorAll("[data-course]").forEach(function (link) {
    link.addEventListener("click", function () {
        document.getElementById("course").value =
            this.getAttribute("data-course");
    });
});

// TRIAL ENQUIRY FORM
// Uses mailto, so the visitor's email app handles sending.
// This website does not claim that an enquiry was sent automatically.
document.getElementById("trialForm").addEventListener(
    "submit",
    function (event) {
        event.preventDefault();

        if (!this.reportValidity()) {
            return;
        }

        const name = document.getElementById("studentName").value.trim();
        const phone = document.getElementById("phone").value.trim();
        const email = document.getElementById("email").value.trim();
        const course = document.getElementById("course").value;
        const subject = document.getElementById("subject").value;
        const message = document.getElementById("message").value.trim();

        const subjectLine = "Free Trial Class Enquiry - " + name;

        const body = [
            "Hello Neuroflex Education,",
            "",
            "I would like to enquire about the two free trial classes.",
            "",
            "Student Name: " + name,
            "Contact Number: " + phone,
            "Email: " + email,
            "Course: " + course,
            "Preferred Subject: " + (subject || "Not specified"),
            "",
            "Additional Information:",
            message || "None",
            "",
            "Please contact me with the available trial class details.",
            "",
            "Thank you."
        ].join("\n");

        const mailto =
            "mailto:neuroflexed@gmail.com" +
            "?subject=" + encodeURIComponent(subjectLine) +
            "&body=" + encodeURIComponent(body);

        const notice = document.getElementById("formMessage");
        notice.style.display = "block";
        notice.textContent =
            "Your email application should open with the enquiry. " +
            "Please click Send in your email application. " +
            "If it does not open, contact neuroflexed@gmail.com directly.";

        window.location.href = mailto;
    }
);
</script>

</body>
</html>
"""


class WebsiteHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            content = HTML.encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)

        elif self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()

        else:
            self.send_error(404, "Page not found")


def open_website():
    webbrowser.open(f"http://localhost:{PORT}")


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", PORT), WebsiteHandler)

    print("=" * 55)
    print("NEUROFLEX EDUCATION WEBSITE")
    print("=" * 55)
    print(f"Website: http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server.")
    print("=" * 55)

    threading.Timer(1.0, open_website).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nWebsite server stopped.")
    finally:
        server.server_close()