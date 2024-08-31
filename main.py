import streamlit as st
from PIL import Image

# Set up the page
st.set_page_config(
    page_title="My Autobiography & Portfolio",
    page_icon="📘",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar for navigation
st.sidebar.title("Navigation")
pages = st.sidebar.radio(
    "Go to",
    ["Home", "Autobiography", "Portfolio", "Contact"],
    format_func=lambda page: {
        "Home": "🏠 Home",
        "Autobiography": "📖 Autobiography",
        "Portfolio": "💼 Portfolio",
        "Contact": "📧 Contact"
    }.get(page)
)

# Header
st.title("Welcome to My Portfolio! 🎉")
st.subheader("Explore My Journey and Projects")

# Home page
if pages == "Home":
    st.image("photos/coverpage.png", use_column_width=True)
    st.write("""
        Hi! I'm Phoebe Kae A. Plasus, a sleep deprived, coffee addicted student, who is passionate about the world of cybersecurity
        and has a knack for making !%#&#* I mean "solving" complex problems and building innovative solutions. Welcome to my personal 
        space where I share my college joureny and connect with like-minded individuals.
    """)


# Autobiography page
elif pages == "Autobiography":
    st.header("About Me")

    # Create two columns with adjusted ratios
    col1, col2 = st.columns([0.70, 0.90])  # Adjust the ratio to give more space to the text

    with col1:
        # Display your picture in the left column
        my_image = Image.open("photos/myphoto.jpg")  # Replace with the path to your image file
        st.image(my_image, caption="That's me!", use_column_width=True)

    with col2:
        # Display the text in the right column
        st.write("""
        Once again I am Phoebe Kae Plasus, You can call me 'Phoebe' or you can call me 'Kae', I am currently a 4th Year student pursuing 
        a Bachelor of Science in Information Technology. Beyond academics, I was actively involved in various clubs and organizations 
        where I've developed not just my technical skills but also my leadership and teamwork capabilities.
                 
        As I near the end of my studies, I'm eager to enter the professional world and apply my skills in the tech industry. My goal is to build a 
        career in cybersecurity, protecting organizations' data and systems from threats.
        """)

    st.markdown("---")

    # Add Personal Profile and Soft Skills
    profile_col, skills_col = st.columns(2)  # Two equal columns

    with profile_col:
        st.write("### PERSONAL PROFILE")
        st.write("**Age:** 22 years old")
        st.write("**Birth date:** January 04, 2002")
        st.write("**Birthplace:** Cebu City")
        st.write("**Gender:** Female")
        st.write("**Religion:** Christian")
        st.write("**Nationality:** Filipino")
        st.write("**Civil Status:** Single")
        st.write("**Weight:** 89.40 lbs.")
        st.write("**Height:** 4ft & 11”")

        

    with skills_col:
        st.write("### SOFT SKILLS")
        st.write("- **Communication & Collaboration**")
        st.write("- **Problem-Solving & Creativity**")
        st.write("- **Adaptability & Flexibility**")
        st.write("- **Leadership & Organization**")
        st.write("- **Time Management**")

    st.markdown("---")

    # Early Days
    st.subheader("Early Days")
    st.write("A glimpse into my early years, where my experiences and upbringing helped shape the values and perspectives I carry today:")

    # Function to load and resize images to fixed dimensions
    def load_image(image_path, width, height):
        img = Image.open(image_path)
        return img.resize((width, height))

    # Set fixed width and height for all images
    fixed_width = 650  # Adjust the width as needed
    fixed_height = 450  # Adjust the height as needed

    # List of images for the slider
    images = [
        "photos/earlydays1.jpg",
        "photos/earlydays2.jpg",
        "photos/earlydays3.jpg",
        "photos/earlydays4.jpg"
    ]

    # Initialize the current image index if it doesn't exist
    if 'current_image' not in st.session_state:
        st.session_state.current_image = 0

    # Navigation buttons with unique keys
    col1, col2, col3 = st.columns([1, 4, 1])

    with col1:
        if st.button("Previous", key="early_days_prev"):
            st.session_state.current_image = (st.session_state.current_image - 1) % len(images)

    with col3:
        if st.button("Next", key="early_days_next"):
            st.session_state.current_image = (st.session_state.current_image + 1) % len(images)

    # Load and display the current image with fixed dimensions
    current_image = load_image(images[st.session_state.current_image], fixed_width, fixed_height)
    st.image(current_image, use_column_width=False)


    st.write("""
        In my early days, I truly valued sleep (hahaha). As a baby, I seemed to enjoy it so much that I kept on sleeping. I was a curious and mischievous 
        child, always fascinated by the little things. According to my father, I would ask odd or unusual questions due to my vivid imagination (which is 
        still very much alive today).

        I was a pretty bright kid, if I do say so myself. I earned honors and did well in English, math, and science from a young age, although I struggled 
        with Filipino—ironically, since I’m a pure-blooded Filipina.

        Despite these achievements, my mischievous side remained strong. One memorable incident from kindergarten involved me and a classmate goofing around 
        before the teacher arrived. It involved a stroller bag, and I ended up dragging my classmate around the classroom in it. We were eventually caught, 
        and as punishment, our bags were hung from the flagpole (hahaha).
    """)

    st.markdown("---")

    # College Journey

    st.subheader("My College Journey")
    st.write("Here’s a glimpse into my journey through college, the experiences I've had, and the lessons I've learned:")

    # Journey Part 1
    
    # Specify the relative path to your photo
    image_path_freshman = 'photos/freshman.jpg'

    with st.expander("🏫 Freshman Year"):
        st.image(image_path_freshman, use_column_width=True)
        st.write("""
            My first year of college was a time of immense learning and adaptation, especially with the onset of the COVID-19 pandemic. As we shifted to 
            online classes during the lockdown, adjusting to the new digital environment was challenging. We had to quickly learn to use various online 
            platforms for classes, assignments, and trying to simulate university life virtually.

            It was particularly tough for me because I started a program in IT with no prior programming knowledge. I didn’t have friends from high school 
            in the same field, as most of them went to different universities, leaving me to navigate this new world on my own. Despite the challenges, I 
            managed to get through it (somehow, haha). Outside of academics, I spent more time with my family, which helped me stay grounded and find 
            balance during such an unpredictable time. This experience made me more resilient and prepared me for the challenges ahead.
        """)

    # Journey Part 2

    # Specify the relative path to your photo
    image_path_sophmore = 'photos/sophmore.jpg'

    with st.expander("💻 Sophomore Year"):
        st.image(image_path_sophmore, use_column_width=True)
        st.write("""
            By sophomore year, I started making a few acquaintances and was gradually grasping the concepts of programming and its foundations. CIT-U adapted 
            quickly to the online environment, and both students and professors became well-adjusted to the platforms we were using. By this point, everything 
            seemed much easier.

            However, it was also during this time that I began experiencing what I now recognize as "Imposter Syndrome." I felt mentally drained and started 
            questioning why I chose this program, even considering shifting to another course. I kept comparing myself to others and felt like I was falling 
            behind. What kept me going was the support and encouragement from my parents, my brothers cheering me on, and advice from a senior I had connected 
            with, who told me, "In this course, you can't survive alone. It's okay to ask questions."

            With that in mind, I allowed myself "to be a beginner" and, despite my introverted nature, started reaching out to classmates and schoolmates I didn’t 
            know. I began asking how they tackled certain topics, seeking advice, and connecting with peers to share our struggles. Before long, I noticed that many 
            of the concepts I had struggled with before became easier.

            I learned that it's okay to struggle with something new—that’s normal. Like a baby learning to walk, it takes time. The key is to be consistent and keep 
            practicing because practice leads to improvement, even if not perfection.
        """)

    # Journey Part 3
    with st.expander("📚 Junior Year"):
        # List of image URLs
        images_junior_year = [
            "photos/me.jpeg",
            "photos/gdsc.jpeg",
            "photos/pf.jpeg",
            "photos/csr.jpeg",
            "photos/devfest.jpeg",
            "photos/googleio.jpeg"
        ]

        # Set fixed width and height for the display box
        box_width = 670
        box_height = 300

        # Function to fit image into a box with black padding if necessary
        def fit_image(image_url, box_width, box_height):
            img = Image.open(image_url)
            img_width, img_height = img.size
            # Calculate the scaling factor and new size
            scale = min(box_width / img_width, box_height / img_height)
            new_width = int(img_width * scale)
            new_height = int(img_height * scale)
            # Resize the image
            img = img.resize((new_width, new_height), Image.LANCZOS)
            # Create a new image with black background
            new_img = Image.new("RGB", (box_width, box_height), (0, 0, 0))
            # Calculate position to center the image
            left = (box_width - new_width) // 2
            top = (box_height - new_height) // 2
            # Paste the resized image onto the black background
            new_img.paste(img, (left, top))
            return new_img

        # Initialize the current image index for junior year if it doesn't exist
        if 'junior_year_image_index' not in st.session_state:
            st.session_state.junior_year_image_index = 0

        # Navigation buttons with unique keys
        col1, col2, col3 = st.columns([1, 4, 1])
        
        with col1:
            if st.button("Previous", key="junior_year_prev"):
                st.session_state.junior_year_image_index = (st.session_state.junior_year_image_index - 1) % len(images_junior_year)

        with col3:
            if st.button("Next", key="junior_year_next"):
                st.session_state.junior_year_image_index = (st.session_state.junior_year_image_index + 1) % len(images_junior_year)

        # Load and fit the current image
        current_image_url = images_junior_year[st.session_state.junior_year_image_index]
        current_image = fit_image(current_image_url, box_width, box_height)
        st.image(current_image, use_column_width=False)

        st.write("""
            Junior year was intense but incredibly rewarding. I took on leadership roles in various clubs, including the Google Developer Student Club, Computer Students' Society, 
            and College Peer Facilitators. I also started working as a barista at the 'Wildcats Lounge' and volunteered outside the university with Google Developers Group and Women 
            Techmakers. This year pushed me out of my shell and challenged me to interact with my peers, despite my introverted nature, helping me grow as both a tech student and a leader.

            This was also the year that sparked my passion for cybersecurity. The curriculum introduced topics related to it, opening my eyes to this exciting field. I began self-learning, 
            reading beyond what was taught in class, and diving deeper into cybersecurity. Although I was still new to the topics and struggled with some of the concepts, I continued to push 
            forward, even without knowing others who shared my interest at the time.

            Balancing academics and student leadership made this the most stressful year for me. Late-night meetings, event planning, a bit of drama, and managing projects all made it hectic. 
            However, looking back now, it was incredibly fulfilling to see the results of my efforts. This year helped me grow not only as a student but also as a person. I made lifelong friends, 
            gained valuable skills, learned important lessons, and created lasting memories. It was truly a year worth remembering.
        """)
    
    # Journey Part 4

    # Specify the relative path to your photo
    image_path_senior = 'photos/candid.jpg'

    with st.expander("🎓 Senior Year"):
        st.image(image_path_senior, use_column_width=True)
        st.write("""
            This is now my final year in college. Oh, I forgot to mention—I’m actually an irregular student due to some challenges during my freshman and sophomore years. After overloading and underloading 
            semesters, taking breaks, and even going to school at 6 AM just for a single class that got canceled, it’s finally my last year. I’m aiming for a January graduation, so do pray for me, haha.

            This year, I’ve stepped down from all my leadership roles and decided not to join any organizations inside or outside of school, except for my ambassadorship with CAMPUS DEVCON (which I 
            was pleasantly surprised to be chosen for). My focus now is on completing my remaining subjects and my OJT. I’ve also picked up where I left off with my cybersecurity self-study, revisiting some 
            class materials. Although this year has just started, it feels like it’s already flying by.

            I pray for everyone to achieve their goals, create lasting memories, meet new friends, get inspired, and inspire others. Let tomorrow’s worries stay with tomorrow—focus on today and the goals you 
            can achieve now. As my time as a student comes to a close, I place all my plans in God’s hands, trusting Him to guide me on the right path. I also pray for strength in my faith this year. My college 
            days may be ending, but my journey in tech is just beginning.
        """)
    st.markdown("---")
    
    # Columns for skills
    st.subheader("Skills")
    col1, col2, col3 = st.columns(3)
    col1.write("🖥️ **Languages**")
    col1.write("- Python\n- JavaScript\n- Java")
    col2.write("🔧 **Frameworks**")
    col2.write("- React\n- Django\n- Spring Boot")
    col3.write("📦 **Tools**")
    col3.write("- Git\n- Burp Suite\n- Metasploit\n- Kali Linux")
    

# Portfolio page
elif pages == "Portfolio":
    st.header("My Projects")

    st.write("Here are the top two projects I've worked on and continue to develop:")
    
    
    # Project 1
    # Specify the relative path to your photo
    image_path_vds = 'photos/vds.png'

    with st.expander("🔍 Project 1:  Vehicle Detection System "):
        st.write("""
            • Developed a real-time car brand and model recognition system using YOLO, 
            focusing on two brands with four models.\n
            • Created and manually annotated a custom dataset to overcome challenges with 
            corrupted pre-exiting datasets. \n
            • Leveraged AI and computer vision to deliver accurate vehicle detection and 
            classification, suitable for traffic monitoring and security applications. 
        """)
        st.image(image_path_vds, use_column_width=True)

    # Project 2
    # Specify the relative path to your photo
    image_path_avr = 'photos/avr.png'

    with st.expander("📊 Project 2: Automated Vehicle Registration and Tracking System"):
        st.write("""
            • Designed and developed an automated vehicle registration and tracking system 
            tailored for our university parking, drastically reducing manual entry errors and 
            speeding up the registration process.\n
            • Streamlined the sticker issuance process by implementing a digital system that 
            verifies applicants’ details and vehicle information, ensuring a secure and efficient 
            distribution of parking stickers\n
            • Enhanced the verification process by integrating features that streamline the review 
            of submitted documents, ensuring that only complete and correctly filled applications 
            are processed.\n
        """)
        st.image(image_path_avr, use_column_width=True)
    
    # Project 3
    # Specify the relative path to your photo
    image_path_ts = 'photos/ts.png'
    with st.expander("📱 Project 3: Text Summarizer"):
        st.write("""
        • Developed an automated text summarizer to efficiently extract key information from lengthy PDFs 
        and text documents, addressing the inefficiencies and potential errors of manual summarization.\n
        • Integrated advanced natural language processing (NLP) techniques using txtai to provide concise, 
        accurate summaries, saving users time and ensuring they capture essential information from their 
        documents.\n
        • Designed a user-friendly interface with Streamlit, allowing users to easily choose between summarizing 
        text or uploading PDF documents for automatic summarization, with PyPDF2 handling the extraction and 
        processing of PDF content.
        """)
        st.image(image_path_ts, use_column_width=True)

# Contact page
elif pages == "Contact":
    st.header("Get in Touch")

    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/phoebe-kae-plasus-574814174/)")
    st.write("🔗 [GitHub](https://github.com/Pbkae)")
    st.write("🔗 [Facebook](https://www.facebook.com/phoebekae.plasus/)")

# Footer
st.markdown("---")
st.markdown("© 2024 Phoebe Kae Plasus - All rights reserved.")
