
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from html import escape
from datetime import datetime
import csv
import os

PORT = 8000
CSV_FILE = "registrations.csv"

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Neuroflex Education is an English Medium institute in Banasree, Dhaka, offering Pre-O Level, O Level, A Level, PTE and IELTS preparation.">
<title>Neuroflex Education | Inspire Minds, Empower Futures</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

<style>
:root {
    --navy: #111d45;
    --blue: #3048a5;
    --purple: #6653bc;
    --cyan: #35bbdb;
    --light: #f5f7ff;
    --white: #ffffff;
    --muted: #69748d;
    --border: #e4e9f5;
    --gradient: linear-gradient(125deg, #253e9a, #7258c8);
}

* { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
    margin: 0;
    font-family: "DM Sans", Arial, sans-serif;
    color: var(--navy);
    background: var(--white);
    line-height: 1.65;
}

h1, h2, h3, h4 {
    font-family: "Outfit", Arial, sans-serif;
    line-height: 1.18;
    margin-top: 0;
}

a { text-decoration: none; color: inherit; }

.container {
    width: min(1160px, 90%);
    margin: auto;
}

section { padding: 92px 0; }

.section-head {
    text-align: center;
    max-width: 730px;
    margin: 0 auto 48px;
}

.eyebrow {
    color: var(--purple);
    text-transform: uppercase;
    font-size: 13px;
    letter-spacing: 2px;
    font-weight: 800;
    margin-bottom: 12px;
    display: inline-block;
}

.section-head h2 {
    font-size: clamp(30px, 4vw, 46px);
    margin-bottom: 15px;
}

.section-head p { color: var(--muted); margin: 0; }

.btn {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    padding: 14px 26px;
    border-radius: 12px;
    font-size: 15px;
    font-weight: 700;
    border: 0;
    cursor: pointer;
    transition: transform .2s, box-shadow .2s;
}

.btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 25px #111d4520;
}

.btn-primary {
    color: white;
    background: var(--gradient);
}

.btn-white {
    color: var(--blue);
    background: white;
}

.btn-outline {
    border: 1px solid #ffffff80;
    color: white;
    background: transparent;
}

header {
    background: white;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 3px 20px #17275310;
}

.nav {
    min-height: 78px;
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

.logo-icon {
    width: 48px;
    height: 48px;
    display: grid;
    place-items: center;
    border-radius: 14px;
    background: var(--gradient);
    color: white;
    font-size: 27px;
}

.logo-name {
    font-family: "Outfit", sans-serif;
    font-size: 21px;
    font-weight: 900;
    line-height: 1.1;
}

.logo-name span { color: var(--purple); }

.logo-tag {
    display: block;
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 1px;
    font-weight: 700;
}

.nav-links {
    display: flex;
    align-items: center;
    gap: 23px;
}

.nav-links a {
    font-size: 14px;
    font-weight: 700;
}

.nav-links a:hover { color: var(--purple); }

.nav-links .nav-cta {
    background: var(--gradient);
    padding: 11px 18px;
    color: white;
    border-radius: 10px;
}

.menu-btn {
    display: none;
    border: 0;
    background: none;
    font-size: 26px;
    cursor: pointer;
    color: var(--navy);
}

.hero {
    background:
        radial-gradient(circle at 85% 20%, #a49af13a, transparent 35%),
        linear-gradient(120deg, #101d4b, #273c91 55%, #5d4db5);
    color: white;
    padding: 110px 0 95px;
    position: relative;
    overflow: hidden;
}

.hero::after {
    content: "";
    position: absolute;
    height: 390px;
    width: 390px;
    border: 65px solid #ffffff09;
    border-radius: 50%;
    right: -120px;
    bottom: -230px;
}

.hero-grid {
    display: grid;
    grid-template-columns: 1.2fr .8fr;
    align-items: center;
    gap: 65px;
    position: relative;
    z-index: 1;
}

.hero-pill {
    display: inline-block;
    padding: 9px 17px;
    border: 1px solid #ffffff55;
    background: #ffffff14;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 23px;
}

.hero h1 {
    font-size: clamp(46px, 6vw, 76px);
    letter-spacing: -2px;
    margin-bottom: 22px;
}

.hero h1 span { color: #77ddf5; }

.hero p {
    color: #e1e5ff;
    font-size: 18px;
    max-width: 570px;
    margin-bottom: 30px;
}

.hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
}

.hero-panel {
    padding: 32px;
    border: 1px solid #ffffff35;
    border-radius: 28px;
    background: #ffffff16;
    backdrop-filter: blur(14px);
    box-shadow: 0 25px 60px #11152f40;
}

.hero-panel h3 { font-size: 26px; }

.hero-panel p {
    font-size: 15px;
    margin-bottom: 23px;
}

.hero-feature {
    display: flex;
    align-items: center;
    gap: 15px;
    background: #ffffff17;
    padding: 16px;
    border-radius: 13px;
    margin-top: 12px;
    font-weight: 700;
}

.feature-icon {
    background: #ffffff20;
    width: 43px;
    height: 43px;
    border-radius: 10px;
    display: grid;
    place-items: center;
    flex-shrink: 0;
    font-size: 23px;
}

.stats {
    background: #f0f3ff;
    padding: 28px 0;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    text-align: center;
    gap: 20px;
}

.stat {
    font-family: "Outfit", sans-serif;
    font-weight: 800;
    font-size: 19px;
    color: var(--blue);
}

.stat small {
    display: block;
    font-family: "DM Sans", sans-serif;
    font-size: 12px;
    font-weight: 500;
    color: var(--muted);
}

.about-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    align-items: center;
    gap: 65px;
}

.about-graphic {
    background: var(--gradient);
    border-radius: 28px;
    min-height: 380px;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 35px;
}

.about-graphic .big-symbol {
    font-size: 95px;
    line-height: 1.3;
}

.about-graphic h3 { font-size: 32px; }

.about-graphic p { max-width: 300px; }

.about-copy h2 { font-size: 43px; }

.about-copy p { color: var(--muted); }

.check-list {
    list-style: none;
    padding: 0;
}

.check-list li {
    display: flex;
    gap: 12px;
    margin-bottom: 15px;
}

.check-list li::before {
    content: "✓";
    color: white;
    background: #31b7d8;
    border-radius: 50%;
    height: 23px;
    width: 23px;
    flex-shrink: 0;
    display: grid;
    place-items: center;
    font-size: 14px;
    font-weight: 900;
}

.bg-light { background: var(--light); }

.card-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
}

.card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 19px;
    padding: 29px;
    transition: .25s;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 35px #17275312;
}

.card-icon {
    height: 58px;
    width: 58px;
    background: #efedff;
    display: grid;
    place-items: center;
    border-radius: 15px;
    font-size: 28px;
    margin-bottom: 20px;
}

.card h3 { font-size: 22px; margin-bottom: 12px; }

.card p {
    color: var(--muted);
    font-size: 14px;
    margin: 0;
}

.subject-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
}

.subject {
    background: white;
    border: 1px solid var(--border);
    border-radius: 13px;
    padding: 19px 17px;
    display: flex;
    gap: 10px;
    align-items: center;
    font-size: 15px;
    font-weight: 700;
}

.subject span {
    color: #31b8d8;
    font-size: 20px;
}

.subject:hover { border-color: var(--purple); }

.course-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
}

.course {
    background: white;
    border: 1px solid var(--border);
    padding: 33px;
    border-radius: 20px;
    position: relative;
    overflow: hidden;
}

.course::before {
    content: "";
    display: block;
    height: 5px;
    background: var(--gradient);
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
}

.course h3 {
    color: var(--blue);
    font-size: 26px;
    margin: 15px 0;
}

.course p {
    font-size: 14px;
    color: var(--muted);
}

.course a {
    font-weight: 800;
    color: var(--purple);
    font-size: 14px;
}

.course-symbol { font-size: 38px; }

.why-banner {
    background: var(--gradient);
    border-radius: 26px;
    color: white;
    padding: 48px;
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: center;
    gap: 25px;
}

.why-banner h2 {
    font-size: 36px;
    margin-bottom: 10px;
}

.why-banner p { margin: 0; color: #e5e5ff; }

.trial {
    background: var(--light);
}

.trial-grid {
    display: grid;
    grid-template-columns: .85fr 1.15fr;
    gap: 55px;
    align-items: start;
}

.trial-copy h2 {
    font-size: 43px;
}

.trial-copy p { color: var(--muted); }

.trial-offer {
    padding: 25px;
    border-radius: 18px;
    background: var(--gradient);
    color: white;
    margin-top: 30px;
}

.trial-offer strong {
    display: block;
    font-size: 26px;
    font-family: "Outfit", sans-serif;
}

.form-card {
    background: white;
    padding: 35px;
    border-radius: 22px;
    box-shadow: 0 15px 50px #20347512;
}

.form-card h3 { font-size: 28px; }

.form-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 17px;
}

.form-group {
    margin-bottom: 18px;
}

.form-group label {
    display: block;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 7px;
}

.form-group input,
.form-group select,
.form-group textarea {
    width: 100%;
    border: 1px solid #dce1ef;
    background: #fafbff;
    border-radius: 10px;
    padding: 13px 14px;
    font: inherit;
    font-size: 14px;
    outline: none;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    border-color: var(--purple);
}

.form-card button { width: 100%; }

.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 50px;
}

.contact h2 { font-size: 40px; }

.contact-info {
    display: flex;
    gap: 17px;
    padding: 18px 0;
    border-bottom: 1px solid var(--border);
}

.contact-icon {
    width: 48px;
    height: 48px;
    background: #eeefff;
    border-radius: 12px;
    display: grid;
    place-items: center;
    font-size: 24px;
    flex-shrink: 0;
}

.contact-info strong { display: block; }

.contact-info a {
    color: var(--blue);
    overflow-wrap: anywhere;
}

.map-wrap {
    border-radius: 20px;
    overflow: hidden;
    min-height: 360px;
    background: #edf1fa;
}

.map-wrap iframe {
    height: 360px;
    width: 100%;
    border: 0;
}

footer {
    background: #101937;
    color: white;
    padding: 60px 0 20px;
}

.footer-grid {
    display: grid;
    grid-template-columns: 2fr 1fr 1.5fr;
    gap: 45px;
}

footer h3 { font-size: 21px; }

footer p, footer a { color: #b7c1df; font-size: 14px; }

footer a {
    display: block;
    margin: 10px 0;
}

footer a:hover { color: white; }

.footer-bottom {
    text-align: center;
    border-top: 1px solid #ffffff25;
    padding-top: 22px;
    margin-top: 45px;
    color: #a9b3d3;
    font-size: 13px;
}

.toast {
    position: fixed;
    right: 25px;
    bottom: 25px;
    padding: 15px 22px;
    background: var(--navy);
    color: white;
    border-radius: 12px;
    box-shadow: 0 10px 30px #0003;
    z-index: 200;
    display: none;
    max-width: 340px;
}

@media(max-width: 960px) {
    .nav-links {
        display: none;
        position: absolute;
        top: 78px;
        left: 0;
        right: 0;
        background: white;
        padding: 25px 6%;
        flex-direction: column;
        align-items: stretch;
        box-shadow: 0 15px 20px #10193717;
    }

    .nav-links.active { display: flex; }
    .menu-btn { display: block; }

    .hero-grid, .about-grid,
    .trial-grid, .contact-grid {
        grid-template-columns: 1fr;
    }

    .hero-panel { max-width: 570px; }

    .card-grid, .course-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .subject-grid { grid-template-columns: repeat(3, 1fr); }

    .footer-grid { grid-template-columns: 1fr 1fr; }
}

@media(max-width: 620px) {
    section { padding: 65px 0; }

    .hero { padding: 75px 0; }
    .hero h1 { font-size: 47px; }

    .card-grid, .course-grid,
    .subject-grid, .stats-grid,
    .form-grid, .footer-grid {
        grid-template-columns: 1fr;
    }

    .stats-grid { gap: 24px; }

    .why-banner {
        grid-template-columns: 1fr;
        padding: 32px;
    }

    .about-copy h2,
    .trial-copy h2 { font-size: 34px; }

    .form-card { padding: 24px; }

    .hero-panel { padding: 23px; }
}
</style>
</head>

<body>

<header>
    <div class="container nav">
        <a href="#home" class="logo">
            <div class="logo-icon">✦</div>
            <div>
                <div class="logo-name">NEUROFLEX <span>EDUCATION</span></div>
                <span class="logo-tag">INSPIRE MINDS · EMPOWER FUTURES</span>
            </div>
        </a>

        <button class="menu-btn" id="menuBtn"
                aria-label="Toggle navigation"
                aria-expanded="false">☰</button>

        <nav class="nav-links" id="navLinks">
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#subjects">Subjects</a>
            <a href="#courses">Courses</a>
            <a href="#why">Why Us</a>
            <a href="#contact">Contact</a>
            <a href="#trial" class="nav-cta">Apply Now</a>
        </nav>
    </div>
</header>

<main>

<section class="hero" id="home">
    <div class="container hero-grid">
        <div>
            <span class="hero-pill">🎓 An English Medium Institute</span>

            <h1>Inspire Minds.<br>
                <span>Empower Futures.</span></h1>

            <p>
                Welcome to Neuroflex Education, where expert teachers,
                focused lessons and a supportive learning environment
                help students build confidence and achieve their goals.
            </p>

            <div class="hero-actions">
                <a class="btn btn-white" href="#trial">Book Free Trial Classes</a>
                <a class="btn btn-outline" href="#courses">Explore Courses</a>
            </div>
        </div>

        <div class="hero-panel">
            <h3>Admissions Are Open!</h3>
            <p>Start your learning journey with Neuroflex Education.</p>

            <div class="hero-feature">
                <div class="feature-icon">📘</div>
                Cambridge &amp; Pearson Edexcel curriculum support
            </div>

            <div class="hero-feature">
                <div class="feature-icon">👩‍🏫</div>
                Experienced English Medium teachers
            </div>

            <div class="hero-feature">
                <div class="feature-icon">🌟</div>
                Modern facilities and student activities
            </div>

            <div class="hero-feature">
                <div class="feature-icon">🎁</div>
                Sign up for 2 free trial classes
            </div>
        </div>
    </div>
</section>

<div class="stats">
    <div class="container stats-grid">
        <div class="stat">Pre-O · O · A Level
            <small>Academic preparation</small>
        </div>
        <div class="stat">Cambridge &amp; Edexcel
            <small>Curriculum-focused teaching</small>
        </div>
        <div class="stat">PTE &amp; IELTS
            <small>English language preparation</small>
        </div>
    </div>
</div>

<section id="about">
    <div class="container about-grid">
        <div class="about-graphic">
            <div class="big-symbol">🎓</div>
            <h3>Learn. Grow. Excel.</h3>
            <p>
                Quality English Medium education in a supportive
                environment.
            </p>
        </div>

        <div class="about-copy">
            <span class="eyebrow">About Neuroflex</span>
            <h2>Education That Helps You Move Forward</h2>

            <p>
                Neuroflex Education is an English Medium institute
                located in Banasree, Dhaka.
            </p>

            <p>
                Our team consists of expert teachers skilled in
                delivering focused, effective lessons. Our instructors
                come from English Medium educational backgrounds,
                bringing knowledge of curriculum, grammar and
                classroom expectations.
            </p>

            <ul class="check-list">
                <li>Focused and effective lessons</li>
                <li>Teachers with English Medium backgrounds</li>
                <li>Support tailored to students' school standards</li>
                <li>A supportive learning environment</li>
            </ul>

            <a href="#contact" class="btn btn-primary">Get in Touch</a>
        </div>
    </div>
</section>

<section class="bg-light" id="why">
    <div class="container">
        <div class="section-head">
            <span class="eyebrow">Why Choose Us</span>
            <h2>What Makes Neuroflex Different?</h2>
            <p>
                We focus on helping every student learn through
                experienced teaching and meaningful support.
            </p>
        </div>

        <div class="card-grid">
            <div class="card">
                <div class="card-icon">👨‍🏫</div>
                <h3>Senior Mentors</h3>
                <p>
                    Authoritative academic guidance from veteran
                    teachers with extensive classroom experience.
                </p>
            </div>

            <div class="card">
                <div class="card-icon">📚</div>
                <h3>English Medium Core</h3>
                <p>
                    Expert instruction tailored to students'
                    English Medium school standards and curricula.
                </p>
            </div>

            <div class="card">
                <div class="card-icon">🏅</div>
                <h3>Professional Experts</h3>
                <p>
                    Dedicated career educators with proven
                    classroom teaching experience.
                </p>
            </div>

            <div class="card">
                <div class="card-icon">🏫</div>
                <h3>Modern Facilities</h3>
                <p>
                    A learning setting designed to support focused
                    study and productive lessons.
                </p>
            </div>

            <div class="card">
                <div class="card-icon">🤝</div>
                <h3>Supportive Environment</h3>
                <p>
                    An encouraging atmosphere where students can
                    ask questions and develop confidence.
                </p>
            </div>

            <div class="card">
                <div class="card-icon">🎨</div>
                <h3>Student Activities</h3>
                <p>
                    Exciting student activities that complement
                    classroom learning and engagement.
                </p>
            </div>
        </div>
    </div>
</section>

<section id="subjects">
    <div class="container">
        <div class="section-head">
            <span class="eyebrow">Our Subjects</span>
            <h2>Explore What You Can Learn</h2>
            <p>
                Academic support across science, mathematics,
                languages, technology and commerce.
            </p>
        </div>

        <div class="subject-grid">
            <div class="subject"><span>✓</span> English</div>
            <div class="subject"><span>✓</span> Physics</div>
            <div class="subject"><span>✓</span> Chemistry</div>
            <div class="subject"><span>✓</span> Biology</div>
            <div class="subject"><span>✓</span> Add / Pure Math</div>
            <div class="subject"><span>✓</span> Math-B / Math-D</div>
            <div class="subject"><span>✓</span> CS / ICT / IT</div>
            <div class="subject"><span>✓</span> Business</div>
            <div class="subject"><span>✓</span> Economics</div>
            <div class="subject"><span>✓</span> Accounting</div>
            <div class="subject"><span>✓</span> Bangla</div>
            <div class="subject"><span>✓</span> Human Biology</div>
        </div>
    </div>
</section>

<section class="bg-light" id="courses">
    <div class="container">
        <div class="section-head">
            <span class="eyebrow">Our Courses</span>
            <h2>Find Your Learning Path</h2>
            <p>
                Choose the preparation programme that matches
                your academic or language-learning goals.
            </p>
        </div>

        <div class="course-grid">
            <div class="course">
                <div class="course-symbol">📗</div>
                <h3>Pre-O Level</h3>
                <p>
                    Build a strong foundation in core subjects
                    before progressing to O Level studies.
                </p>
                <a href="#trial">Enquire Now →</a>
            </div>

            <div class="course">
                <div class="course-symbol">📘</div>
                <h3>O Level</h3>
                <p>
                    Subject-based academic preparation with
                    a focus on understanding and exam readiness.
                </p>
                <a href="#trial">Enquire Now →</a>
            </div>

            <div class="course">
                <div class="course-symbol">🎓</div>
                <h3>A Level</h3>
                <p>
                    Advanced subject preparation supporting
                    higher-level academic learning.
                </p>
                <a href="#trial">Enquire Now →</a>
            </div>

            <div class="course">
                <div class="course-symbol">🌐</div>
                <h3>PTE</h3>
                <p>
                    English language test preparation for
                    students planning their next steps.
                </p>
                <a href="#trial">Enquire Now →</a>
            </div>

            <div class="course">
                <div class="course-symbol">🗣️</div>
                <h3>Online IELTS</h3>
                <p>
                    IELTS preparation delivered through
                    online learning sessions.
                </p>
                <a href="#trial">Enquire Now →</a>
            </div>

            <div class="course">
                <div class="course-symbol">✨</div>
                <h3>Trial Classes</h3>
                <p>
                    Experience the teaching environment
                    before making an enrolment decision.
                </p>
                <a href="#trial">Register Now →</a>
            </div>
        </div>

        <p style="text-align:center;color:var(--muted);margin-top:26px;font-size:13px">
            Curriculum support: Cambridge International Education
            and Pearson Edexcel.
        </p>
    </div>
</section>

<section>
    <div class="container">
        <div class="why-banner">
            <div>
                <h2>Ready to Excel?</h2>
                <p>
                    Admissions are open. Sign up for 2 free trial classes
                    and experience Neuroflex Education.
                </p>
            </div>
            <a href="#trial" class="btn btn-white">Register for Free</a>
        </div>
    </div>
</section>

<section class="trial" id="trial">
    <div class="container trial-grid">
        <div class="trial-copy">
            <span class="eyebrow">Admissions Open</span>
            <h2>Take the First Step Towards Your Future</h2>
            <p>
                Interested in joining Neuroflex Education?
                Complete the form and our team can discuss
                suitable courses and trial classes with you.
            </p>

            <div class="trial-offer">
                <strong>🎁 2 Free Trial Classes</strong>
                <p style="color:#eae9ff;margin-bottom:0">
                    Register your interest to avail the
                    trial-class offer advertised in our leaflet.
                    Availability is subject to confirmation.
                </p>
            </div>

            <p style="margin-top:25px">
                Prefer to speak with us directly?
                <br>
                <strong>
                    <a href="tel:+8801845440528">
                        +880 1845-440528
                    </a>
                </strong>
            </p>
        </div>

        <div class="form-card">
            <h3>Trial Class Registration</h3>
            <p style="color:var(--muted);font-size:14px">
                Fill in your details to register your interest.
            </p>

            <form id="registrationForm">
                <div class="form-grid">
                    <div class="form-group">
                        <label for="student">Student's Name *</label>
                        <input id="student" name="student"
                               placeholder="Full name"
                               required maxlength="100">
                    </div>

                    <div class="form-group">
                        <label for="guardian">Parent / Guardian</label>
                        <input id="guardian" name="guardian"
                               placeholder="Guardian's name"
                               maxlength="100">
                    </div>
                </div>

                <div class="form-grid">
                    <div class="form-group">
                        <label for="phone">Phone Number *</label>
                        <input id="phone" name="phone" type="tel"
                               placeholder="+880..."
                               required maxlength="25">
                    </div>

                    <div class="form-group">
                        <label for="email">Email Address</label>
                        <input id="email" name="email" type="email"
                               placeholder="example@email.com"
                               maxlength="150">
                    </div>
                </div>

                <div class="form-grid">
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
                            <option value="">Choose a subject</option>
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
                            <option>Other / Not Sure</option>
                        </select>
                    </div>
                </div>

                <div class="form-group">
                    <label for="message">Additional Message</label>
                    <textarea id="message" name="message"
                              rows="4" maxlength="1000"
                              placeholder="Tell us anything we should know..."></textarea>
                </div>

                <button type="submit" class="btn btn-primary">
                    Submit Registration
                </button>

                <p style="font-size:12px;color:var(--muted);margin-top:15px">
                    Your details are submitted to this website's server.
                    The institute must confirm your registration separately.
                </p>
            </form>
        </div>
    </div>
</section>

<section class="contact" id="contact">
    <div class="container">
        <div class="section-head">
            <span class="eyebrow">Contact Us</span>
            <h2>We Would Love to Hear From You</h2>
            <p>
                Contact Neuroflex Education for course enquiries,
                admissions and trial-class information.
            </p>
        </div>

        <div class="contact-grid">
            <div>
                <h2>Visit Our Institute</h2>

                <div class="contact-info">
                    <div class="contact-icon">📍</div>
                    <div>
                        <strong>Address</strong>
                        Ground Floor, House 15, Road 3,<br>
                        Block B, Banasree, Dhaka 1219,
                        Bangladesh
                    </div>
                </div>

                <div class="contact-info">
                    <div class="contact-icon">📞</div>
                    <div>
                        <strong>Phone</strong>
                        <a href="tel:+8801845440528">
                            +880 1845-440528
                        </a>
                    </div>
                </div>

                <div class="contact-info">
                    <div class="contact-icon">✉️</div>
                    <div>
                        <strong>Email</strong>
                        <a href="mailto:neuroflexed@gmail.com">
                            neuroflexed@gmail.com
                        </a>
                    </div>
                </div>

                <div class="contact-info">
                    <div class="contact-icon">📱</div>
                    <div>
                        <strong>Follow Us</strong>
                        <a href="https://www.facebook.com/neuroflexed"
                           target="_blank" rel="noopener noreferrer">
                            Facebook: neuroflexed
                        </a>
                        <a href="https://www.instagram.com/neuroflexed"
                           target="_blank" rel="noopener noreferrer">
                            Instagram: neuroflexed
                        </a>
                    </div>
                </div>

                <a class="btn btn-primary"
                   style="margin-top:25px"
                   href="https://www.google.com/maps/search/?api=1&query=House+15+Road+3+Block+B+Banasree+Dhaka+1219"
                   target="_blank" rel="noopener noreferrer">
                    Get Directions
                </a>
            </div>

            <div class="map-wrap">
                <iframe
                    title="Neuroflex Education location"
                    src="https://www.google.com/maps?q=House%2015%20Road%203%20Block%20B%20Banasree%20Dhaka%201219&output=embed"
                    loading="lazy"
                    referrerpolicy="no-referrer-when-downgrade">
                </iframe>
            </div>
        </div>
    </div>
</section>

</main>

<footer>
    <div class="container">
        <div class="footer-grid">
            <div>
                <h3>NEUROFLEX EDUCATION</h3>
                <p>Inspire Minds. Empower Futures.</p>
                <p>
                    An English Medium institute offering
                    academic support and English language
                    preparation in Banasree, Dhaka.
                </p>
            </div>

            <div>
                <h3>Quick Links</h3>
                <a href="#about">About Us</a>
                <a href="#subjects">Our Subjects</a>
                <a href="#courses">Courses</a>
                <a href="#trial">Free Trial Classes</a>
                <a href="#contact">Contact</a>
            </div>

            <div>
                <h3>Contact Information</h3>
                <p>
                    House 15, Road 3, Block B,<br>
                    Banasree, Dhaka 1219
                </p>
                <a href="tel:+8801845440528">
                    +880 1845-440528
                </a>
                <a href="mailto:neuroflexed@gmail.com">
                    neuroflexed@gmail.com
                </a>
                <a href="https://www.facebook.com/neuroflexed"
                   target="_blank" rel="noopener noreferrer">Facebook</a>
                <a href="https://www.instagram.com/neuroflexed"
                   target="_blank" rel="noopener noreferrer">Instagram</a>
            </div>
        </div>

        <div class="footer-bottom">
            © <span id="year"></span> Neuroflex Education.
            All Rights Reserved.
        </div>
    </div>
</footer>

<div id="toast" class="toast" role="status" aria-live="polite"></div>

<script>
const menuBtn = document.getElementById("menuBtn");
const navLinks = document.getElementById("navLinks");

menuBtn.addEventListener("click", () => {
    const active = navLinks.classList.toggle("active");
    menuBtn.setAttribute("aria-expanded", String(active));
    menuBtn.textContent = active ? "✕" : "☰";
});

navLinks.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", () => {
        navLinks.classList.remove("active");
        menuBtn.setAttribute("aria-expanded", "false");
        menuBtn.textContent = "☰";
    });
});

document.getElementById("year").textContent =
    new Date().getFullYear();

const form = document.getElementById("registrationForm");
const toast = document.getElementById("toast");

function showToast(message) {
    toast.textContent = message;
    toast.style.display = "block";
    setTimeout(() => {
        toast.style.display = "none";
    }, 5000);
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const submitButton = form.querySelector("button[type=submit]");
    const formData = new FormData(form);
    const data = new URLSearchParams(formData);

    submitButton.disabled = true;
    submitButton.textContent = "Submitting...";

    try {
        const response = await fetch("/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: data.toString()
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.message || "Registration failed.");
        }

        form.reset();
        showToast(
            "Your registration enquiry was saved successfully. " +
            "Please contact the institute to confirm your classes."
        );
    } catch (error) {
        showToast(error.message || "Unable to submit the form.");
    } finally {
        submitButton.disabled = false;
        submitButton.textContent = "Submit Registration";
    }
});
</script>

</body>
</html>
"""


class NeuroflexHandler(BaseHTTPRequestHandler):

    def send_content(self, content, status=200, content_type="text/html"):
        encoded = content.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type + "; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def send_json(self, success, message, status=200):
        import json
        payload = json.dumps({
            "success": success,
            "message": message
        })
        self.send_content(payload, status, "application/json")

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.send_content(HTML)
        else:
            self.send_content("<h1>404 - Page Not Found</h1>", 404)

    def do_POST(self):
        if self.path != "/register":
            self.send_json(False, "Unknown endpoint.", 404)
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))

            if length <= 0 or length > 10000:
                self.send_json(False, "Invalid form size.", 400)
                return

            body = self.rfile.read(length).decode("utf-8")
            params = parse_qs(body, keep_blank_values=True)

            def get_value(key, limit=100):
                return params.get(key, [""])[0].strip()[:limit]

            student = get_value("student")
            guardian = get_value("guardian")
            phone = get_value("phone", 25)
            email = get_value("email", 150)
            course = get_value("course")
            subject = get_value("subject")
            message = get_value("message", 1000)

            valid_courses = {
                "Pre-O Level", "O Level", "A Level",
                "PTE", "Online IELTS"
            }

            if not student or not phone or course not in valid_courses:
                self.send_json(
                    False,
                    "Please enter your name, phone and a valid course.",
                    400
                )
                return

            if len(phone) < 7:
                self.send_json(False, "Enter a valid phone number.", 400)
                return

            # Prevent spreadsheet formula execution when CSV is opened.
            def csv_safe(value):
                if value and value[0] in ("=", "+", "-", "@"):
                    return "'" + value
                return value

            row = [
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                student, guardian, phone, email,
                course, subject, message
            ]

            headers = [
                "Date", "Student", "Guardian", "Phone",
                "Email", "Course", "Subject", "Message"
            ]

            file_exists = os.path.exists(CSV_FILE)

            with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                if not file_exists or os.path.getsize(CSV_FILE) == 0:
                    writer.writerow(headers)

                writer.writerow([csv_safe(str(value)) for value in row])

            print(f"New registration: {escape(student)} | {course}")

            self.send_json(
                True,
                "Registration enquiry saved successfully."
            )

        except (ValueError, UnicodeDecodeError):
            self.send_json(False, "Invalid request.", 400)

        except OSError:
            self.send_json(False, "Unable to save registration.", 500)


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", PORT), NeuroflexHandler)

    print("=" * 55)
    print("     NEUROFLEX EDUCATION WEBSITE")
    print("=" * 55)
    print(f"Website: http://localhost:{PORT}")
    print("Registration data: registrations.csv")
    print("Press Ctrl+C to stop the server.")
    print("=" * 55)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()
