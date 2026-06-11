with open(r"c:\Users\Wajiz.pk\OneDrive\Documents\Desktop\abc\muskan_portfolio-1 (1).html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Let's find where the SK EVENTS CLONE starts and replace from line 523 onwards
# Line numbers are 1-based in the editor, so index 522 in the list

# Let's write the new content starting from line 523
new_content = '''  <!-- SK EVENTS CLONE -->
  <div class="brand-block">
    <div class="brand-block-info">
      <h3 class="brand-block-title">DROPS.COM</h3>
      <div class="brand-block-handle">Event Brand · Karachi</div>
      <p class="brand-block-desc">Social Media Marketing Specialist | Driving Growth & Conversion

 <b>Graphic Designer | Drops.com </b>
<p><b>Visual Strategy & Brand Growth:</b> Conceptualized and executed high-conversion visual assets that directly contributed to a substantial increase in total sales performance.

<p><b>Content Optimization:</b></p> Leveraged data-driven design principles to create engaging social media content, resulting in measurable improvements in audience interaction and brand reach.

<p><b>Campaign Execution:</b></p> Collaborated with the marketing team to design cohesive visual campaigns that translated audience engagement into consistent revenue growth.

<p><b>Creative Problem Solving:</b></p> Utilized technical design expertise to refine ad creatives and promotional materials, consistently exceeding sales targets and optimizing the brand's digital presence.</div>
    
<div class="slider" id="sk-2">
  <div class="slides-wrap">
    <div class="slide active"><img src="https://i.imgur.com/1aU6pW8.jpg" alt="DROPS - Zidane"></div>
    <div class="slide"><img src="https://i.imgur.com/zpXwQ1W.jpg" alt="DROPS - Voyage"></div>
    <div class="slide"><img src="https://i.imgur.com/cU6w8E7.jpg" alt="DROPS - Snickers"></div>
    <div class="slide"><img src="https://i.imgur.com/rV9ZkP4.jpg" alt="DROPS - Professor"></div>
  </div>
  <button class="sl-btn prev" onclick="slide('sk-2',-1)">&#8249;</button>
  <button class="sl-btn next" onclick="slide('sk-2',1)">&#8250;</button>
  <div class="dots">
    <span class="dot active" onclick="goTo('sk-2',0)"></span>
    <span class="dot" onclick="goTo('sk-2',1)"></span>
    <span class="dot" onclick="goTo('sk-2',2)"></span>
    <span class="dot" onclick="goTo('sk-2',3)"></span>
  </div>
</div>
  </div>

</section>

<section id="experience">
  <div class="section-eyebrow">Experience</div>
  <h2 class="section-title">Work History</h2>
  <p class="section-sub">Building brands and closing deals — from social media to sales.</p>
  <div class="timeline">
    <div class="tl-item">
      <div class="tl-dot"></div>
      <div class="tl-date">Apr – Jun 2026</div>
      <div class="tl-role">International Sales Executive</div>
      <div class="tl-company">Source Code — Karachi</div>
      <ul class="tl-bullets">
        <li>Cold-called international clients across multiple markets; managed full-cycle communication from first contact to deal closure.</li>
        <li>Handled objections and maintained follow-up across a structured sales pipeline.</li>
        <li>Built cross-cultural client rapport with professionalism across time zones.</li>
      </ul>
    </div>
    <div class="tl-item">
      <div class="tl-dot"></div>
      <div class="tl-date">2023 – 2025</div>
      <div class="tl-role">Social Media Manager & Brand Strategist</div>
      <div class="tl-company">Freelance / Remote</div>
      <ul class="tl-bullets">
        <li>Grew @emayaaa_store from near-zero to 25.2K followers — top reel hit 26.6K views.</li>
        <li>Grew @amavelaura (skincare) from 4.7K to 11.2K followers; rebuilt content strategy and brand voice.</li>
        <li>Built The Royal Essential (luxury perfume) from zero: undefined identity → full ad suite, live website, active presence.</li>
        <li>Art-directed complete product visual suite for Drops fragrance line.</li>
        <li>Managed 5 brands simultaneously — all organic growth, zero paid media.</li>
      </ul>
    </div>
    <div class="tl-item">
      <div class="tl-dot"></div>
      <div class="tl-date">2024</div>
      <div class="tl-role">Marketing Intern</div>
      <div class="tl-company">Digital Marketing Agency</div>
      <ul class="tl-bullets">
        <li>Supported campaign execution, influencer coordination, and competitor research.</li>
        <li>Tracked performance metrics and adapted content tone across different brand voices.</li>
      </ul>
    </div>
    <div class="tl-item">
      <div class="tl-dot"></div>
      <div class="tl-date">2023</div>
      <div class="tl-role">Chat-Based Sales & Customer Support Intern</div>
      <div class="tl-company">Software House — Karachi</div>
      <ul class="tl-bullets">
        <li>Closed inbound sales across chat platforms with high client satisfaction scores.</li>
        <li>Gained hands-on CRM and customer engagement experience in a live tech environment.</li>
      </ul>
    </div>
    <div class="tl-item">
      <div class="tl-dot"></div>
      <div class="tl-date">2020 – 2022</div>
      <div class="tl-role">Event Coordinator</div>
      <div class="tl-company">SK Events & Jaztas — Karachi</div>
      <ul class="tl-bullets">
        <li>Coordinated full event lifecycle: pre-event promotion, live social media coverage, and post-event recap reels.</li>
      </ul>
    </div>
  </div>
</section>

<section id="certs">
  <div class="section-eyebrow">Credentials</div>
  <h2 class="section-title">Certifications</h2>
  <div class="certs-grid">
    <div class="cert-card">
      <div class="cert-icon">🎓</div>
      <h3>Digital Marketing</h3>
      <p>Aligarh Institute of Technology, Karachi<br>Mar 2024 – Jun 2024 · CEP Programme</p>
    </div>
    <div class="cert-card">
      <div class="cert-icon">🏆</div>
      <h3>Certificate of Appreciation</h3>
      <p>Taste & Trends Popup Market · SK Events & Jaztas<br>October 15, 2024</p>
    </div>
    <div class="cert-card">
      <div class="cert-icon">💻</div>
      <h3>Diploma in Software Engineering</h3>
      <p>Currently Pursuing<br>Expanding into tech + marketing</p>
    </div>
  </div>
</section>

<div class="contact-section" id="contact">
  <h2>Ready to build<br>something iconic?</h2>
  <p>Social media strategy, content creation, graphic design, or events — I'm here for it all.<br>Open to full-time & freelance opportunities.</p>
  <a href="mailto:muskanhaider0106@gmail.com" class="email-badge">muskanhaider0106@gmail.com</a>
</div>

<footer>© 2026 Muskan Haider · Social Media Strategist & Brand Builder · Karachi, Pakistan</footer>


<script>
const state = {};
function getState(id) {
  if (!state[id]) {
    const el = document.getElementById(id);
    state[id] = { idx: 0, slides: el.querySelectorAll('.slide'), dots: el.querySelectorAll('.dot') };
  }
  return state[id];
}
function goTo(id, n) {
  const s = getState(id);
  s.slides[s.idx].classList.remove('active');
  s.dots[s.idx].classList.remove('active');
  s.idx = (n + s.slides.length) % s.slides.length;
  s.slides[s.idx].classList.add('active');
  s.dots[s.idx].classList.add('active');
}
function slide(id, dir) {
  const s = getState(id);
  goTo(id, s.idx + dir);
}
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const t = document.querySelector(a.getAttribute('href'));
    if(t){ e.preventDefault(); t.scrollIntoView({behavior:'smooth'}); }
  });
});
</script>
<script style="display:none">
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const t = document.querySelector(a.getAttribute('href'));
    if(t){ e.preventDefault(); t.scrollIntoView({behavior:'smooth'}); }
  });
});
</script>
</body>
</html>
'''

# Now, let's keep everything up to line 523 and then append the new content
final_lines = lines[:522]
final_lines.append(new_content)

with open(r"c:\Users\Wajiz.pk\OneDrive\Documents\Desktop\abc\muskan_portfolio-1 (1).html", "w", encoding="utf-8") as f:
    f.writelines(final_lines)

print("Successfully updated the slider!")