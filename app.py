from flask import Flask,jsonify, send_from_directory, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

# Set the base directory as the 'goodweb' folder
BASE_DIR = "C:/Users/shree computer/Desktop/sample1/goodweb"
#EXCEL_FILE_PATH = os.path.join(BASE_DIR, 'contact_form_data.xlsx')
EXCEL_FILE_PATH = r"C:\Users\shree computer\Desktop\sample1\goodweb\contact_form_data.xlsx"

images_dir=r"C:\Users\shree computer\Desktop\sample1\goodweb\images"

# Serve the index.html file
@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')


@app.route('/index.html')
def index_html():
    return send_from_directory(BASE_DIR, 'index.html')

# Serve the contact.html file (without .html in the URL)
@app.route('/contact')
def contact():
    return send_from_directory(BASE_DIR, 'contact.html')

# Serve the contact.html file (with .html in the URL)
@app.route('/contact.html')
def contact_html():
    return send_from_directory(BASE_DIR, 'contact.html')

@app.route('/courses.html')
def courses_html():
    return send_from_directory(BASE_DIR, 'courses.html')

@app.route('/internship.html')
def internship_html():
    return send_from_directory(BASE_DIR, 'internship.html')

@app.route('/services.html')
def services_html():
    return send_from_directory(BASE_DIR, 'services.html')


@app.route('/about-us.html')
def about_us_html():
    return send_from_directory(BASE_DIR, 'about-us.html')

@app.route('/team.html')
def team_html():
    return send_from_directory(BASE_DIR, 'team.html')


@app.route('/java.html')
def java_html():
    return send_from_directory(BASE_DIR, 'java.html')
@app.route('/python.html')
def python_html():
    return send_from_directory(BASE_DIR, 'python.html')
@app.route('/data_science.html')
def data_science_html():
    return send_from_directory(BASE_DIR, 'data_science.html')
@app.route('/web_devlopmet.html')
def web_development_html():
    return send_from_directory(BASE_DIR, 'web_devlopmet.html')
@app.route('/candcpp.html')
def c_and_cpp_html():
    return send_from_directory(BASE_DIR, 'candcpp.html')


@app.route('/style.css')
def serve_style_css():
    return send_from_directory(BASE_DIR,'style.css')

# Serve specific CSS files
@app.route('/css/animate.css')
def serve_animate_css():
    return send_from_directory(os.path.join(BASE_DIR, 'css'), 'animate.css')

@app.route('/css/bootstrap-theme.min.css')
def serve_bootstrap_theme_min_css():
    return send_from_directory(os.path.join(BASE_DIR, 'css'), 'bootstrap-theme.css')

@app.route('/css/bootstrap-theme.min.css')
def serve_bootstrap_css():
    return send_from_directory(os.path.join(BASE_DIR, 'css'), 'bootstrap.css')

@app.route('/css/bootstrap.min.css')
def serve_bootstrap_min_css():
    return send_from_directory(os.path.join(BASE_DIR, 'css'), 'bootstrap.min.css')


@app.route('/css/custom.css')
def serve_custom_css():
    return send_from_directory(os.path.join(BASE_DIR, 'css'), 'custom.css')

@app.route('/css/flaticon.css')
def serve_flaticon_css():
    return send_from_directory(os.path.join(BASE_DIR, 'css'), 'flaticon.css')

@app.route('/css/font-awesome.css')
def serve_font_awesome_css():
    return send_from_directory(os.path.join(BASE_DIR, 'css'), 'font-awesome.css')

@app.route('/css/font-awesome.min.css')
def serve_font_awesome_min_css():
    return send_from_directory(os.path.join(BASE_DIR, 'css'), 'font-awesome.min.css')

@app.route('/css/icomoon.css')
def serve_icomoon_css():
    return send_from_directory(os.path.join(BASE_DIR, 'css'), 'icomoon.css')

@app.route('/css/owl.carousel.css')
def serve_owl_carousel_css():
    return send_from_directory(os.path.join(BASE_DIR, 'css'), 'owl.carousel.css')



@app.route('/css/responsive.css')
def serve_responsive_css():
    return send_from_directory(os.path.join(BASE_DIR, 'css'), 'responsive.css')






# Serve specific js files
# js file
@app.route('/js/app.js')
def serve_app_js():
    return send_from_directory(os.path.join(BASE_DIR, 'js'), 'app.js')

@app.route('/js/all.js')
def serve_all_js():
    return send_from_directory(os.path.join(BASE_DIR, 'js'), 'all.js')

@app.route('/js/custom.js')
def serve_custom_js():
    return send_from_directory(os.path.join(BASE_DIR, 'js'), 'custom.js')

# js file
@app.route('/js/hoverdir.js')
def serve_hoverdir_js():
    return send_from_directory(os.path.join(BASE_DIR, 'js'), 'hoverdir.js')

# js file
@app.route('/js/modernizer.js')
def serve_modernizer_js():
    return send_from_directory(os.path.join(BASE_DIR, 'js'), 'modernizer.js')

@app.route('/js/portfolio.js')
def serve_portfolio_js():
    return send_from_directory(os.path.join(BASE_DIR, 'js'), 'portfolio.js')
# fonts
@app.route('/fonts/Flaticon.eot')
def serve_Flaticon_eot():
    return send_from_directory(os.path.join(BASE_DIR, 'fonts'), 'Flaticon.eot')

@app.route('/fonts/Flaticon.svg')
def serve_Flaticon_svg():
    return send_from_directory(os.path.join(BASE_DIR, 'fonts'), 'Flaticon.svg')

@app.route('/fonts/Flaticon.ttf')
def serve_Flaticon_ttf():
    return send_from_directory(os.path.join(BASE_DIR, 'fonts'), 'Flaticon.ttf')


@app.route('/fonts/Flaticon.woff')
def serve_Flaticon_woff():
    return send_from_directory(os.path.join(BASE_DIR, 'fonts'), 'Flaticon.woff')

@app.route('/fonts/fontawesome-webfonts.eot')
def serve_fontawesome_webfonts_eot():
    return send_from_directory(os.path.join(BASE_DIR, 'fonts'), 'fontawesome-webfonts.eot')

@app.route('/fonts/fontawesome-webfonts.svg')
def serve_fontawesome_webfonts_svg():
    return send_from_directory(os.path.join(BASE_DIR, 'fonts'), 'fontawesome-webfonts.svg')

@app.route('/fonts/fontawesome-webfonts.ttf')
def serve_fontawesome_webfonts_ttf():
    return send_from_directory(os.path.join(BASE_DIR, 'fonts'), 'fontawesome-webfonts.ttf')

@app.route('/images/logos/shorat.png')
def serve_images_logos_shorat():
    return send_from_directory(os.path.join(BASE_DIR, 'images'), 'shorat.png')

@app.route('/images/logos/logo.png')
def serve_images_logos_logo():
    return send_from_directory(os.path.join(BASE_DIR, 'images'), 'logo.png')







@app.route('/about_01.jpg')
def serve_about_01():
    return send_from_directory(BASE_DIR,'about_01.jpg')

@app.route('/about_02.jpg')
def serve_about_02():
    return send_from_directory(BASE_DIR,'about_02.jpg')

@app.route('/slider_01.jpg')
def serve_slider_01():
    return send_from_directory(BASE_DIR,'slider_01.jpg')
@app.route('/slider_02.jpg')
def serve_slider_02():
    return send_from_directory(BASE_DIR,'slider_02.jpg')
@app.route('/slider_03.jpg')
def serve_slider_03():
    return send_from_directory(BASE_DIR,'slider_03.jpg')
@app.route('/parallax_04.jpg')
def serve_parallax_04():
    return send_from_directory(BASE_DIR,'parallax_04.jpg')
@app.route('/akshay_photo.png')
def serve_akshay_photo():
    return send_from_directory(BASE_DIR,'akshay_photo.png')

@app.route('/inner-bg.jpg')
def serve_inner_bg():
    return send_from_directory(BASE_DIR,'inner-bg.jpg')
@app.route('/Python.jpg')
def serve_Python():
    return send_from_directory(BASE_DIR,'Python.jpg')
@app.route('/java.jpg')
def serve_java():
    return send_from_directory(BASE_DIR,'java.jpg')
@app.route('/Web-Development.jpg')
def serve_Web():
    return send_from_directory(BASE_DIR,'Web-Development.jpg')
@app.route('/appdev.jpeg')
def serve_appdev():
    return send_from_directory(BASE_DIR,'appdev.jpeg')
@app.route('/datascience.png')
def serve_data_science():
    return send_from_directory(BASE_DIR,'datascience.png')
@app.route('/c_and_cpp.jpg')
def serve_c_and_cpp():
    return send_from_directory(BASE_DIR,'c_and_cpp.jpg')
@app.route('/data_analytics.jpg')
def serve_Data_analytics():
    return send_from_directory(BASE_DIR,'data_analytics.jpg')
@app.route('/autocad.jpeg')
def serve_auto_cad():
    return send_from_directory(BASE_DIR,'autocad.jpeg')
@app.route('/soft-testing.jpg')
def serve_Soft_test():
    return send_from_directory(BASE_DIR,'soft-testing.jpg')
@app.route('/internshipimage (2).jpg')
def internship_image():
    return send_from_directory(BASE_DIR,'internshipimage (2).jpg')
@app.route('/soft.jpeg')
def soft_image():
    return send_from_directory(BASE_DIR,'soft.jpeg')
@app.route('/autocad2.jpg')
def auto_image():
    return send_from_directory(BASE_DIR,'autocad2.jpg')
@app.route('/data_analyst2.jpeg')
def Data_image():
    return send_from_directory(BASE_DIR,'data_analyst2.jpeg')
@app.route('/data_science2.jpg')
def data_science2_image():
    return send_from_directory(BASE_DIR,'data_science2.jpg')
@app.route('/Python_full_stack.jpg')
def Python_full_stack_image():
    return send_from_directory(BASE_DIR,'Python_full_stack.jpg')
@app.route('/flutter_dev.jpg')
def flutter_dev_image():
    return send_from_directory(BASE_DIR,'flutter_dev.jpg')
@app.route('/AWS.jpg')
def aws_image():
    return send_from_directory(BASE_DIR,'AWS.jpg')
@app.route('/graphic_design.jpg')
def graphic_design_image():
    return send_from_directory(BASE_DIR,'graphic_design.jpg')
@app.route('/sohil.jpg')
def sohil_image():
    return send_from_directory(BASE_DIR,'sohil.jpg')
@app.route('/loader.gif')
def loader_image():
    return send_from_directory(BASE_DIR,'loader.gif')
@app.route('/sanyukta.png')
def sanyukta_image():
    return send_from_directory(BASE_DIR,'sanyukta.png')
@app.route('/harshada.jpg')
def harshada_image():
    return send_from_directory(BASE_DIR,'harshada.jpg')
@app.route('/vaishali.jpg')
def vaishali_image():
    return send_from_directory(BASE_DIR,'vaishali.jpg')





# Serve JS files
@app.route('/<filename>.js')
def serve_js(filename):
    return send_from_directory(BASE_DIR, f'{filename}.js')



# Serve font files
@app.route('/fonts/<filename>')
def serve_fonts(filename):
    return send_from_directory(os.path.join(BASE_DIR, 'fonts'), filename)

# Handle form submissions
@app.route('/submit_form', methods=['POST'])
def submit_form():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']
    comments = request.form['comments']

    # Save the form data to an Excel file
    if os.path.exists(EXCEL_FILE_PATH):
        # Load existing data if the file exists
        df_existing = pd.read_excel(EXCEL_FILE_PATH)
    else:
        # Create a new DataFrame with the correct columns if the file does not exist
        df_existing = pd.DataFrame(columns=['First Name', 'Last Name', 'Email', 'Phone', 'Comments'])

    # Create a new DataFrame with the form data
    df_new = pd.DataFrame([[first_name, last_name, email, phone, comments]], 
                          columns=['First Name', 'Last Name', 'Email', 'Phone', 'Comments'])

    # Concatenate existing data with new data
    df_updated = pd.concat([df_existing, df_new], ignore_index=True)
    
    # Save the updated DataFrame to the specified Excel file
    df_updated.to_excel(EXCEL_FILE_PATH, index=False)

    return jsonify({'message': 'Success'}), 200
   
if __name__ == '__main__':
    app.run(debug=True)
