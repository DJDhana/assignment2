# # class CareerPage:
# #     def _init_(self):
# #         self.job_posts = []

# #     class Admin:
# #         def _init_(self, career_page):
# #             self.career_page = career_page

# #         def add_job_post(self, title, description, requirements):
# #             job_post = {
# #                 'title': title,
# #                 'description': description,
# #                 'requirements': requirements,
# #                 'applications': []
# #             }
# #             self.career_page.job_posts.append(job_post)

# #         def view_applications(self, job_index):
# #             if 0 <= job_index < len(self.career_page.job_posts):
# #                 job_post = self.career_page.job_posts[job_index]
# #                 return job_post['applications']
# #             else:
# #                 return "Job not found."

# #     class User:
# #         def _init_(self, career_page):
# #             self.career_page = career_page

# #         def view_jobs(self):
# #             return self.career_page.job_posts

# #         def apply_for_job(self, job_index, user_info):
# #             if 0 <= job_index < len(self.career_page.job_posts):
# #                 job_post = self.career_page.job_posts[job_index]
# #                 job_post['applications'].append(user_info)
# #                 return "Application submitted successfully."
# #             else:
# #                 return "Job not found."

# # # Example usage with user input:
# # career_page = CareerPage()

# # while True:
# #     print("1. Admin\n2. User\n3. Quit")
# #     choice = input("Enter your choice: ")

# #     if choice == '1':
# #         admin = career_page.Admin(career_page)
# #         title = input("Enter job title: ")
# #         description = input("Enter job description: ")
# #         requirements = input("Enter job requirements: ")
# #         admin.add_job_post(title, description, requirements)
# #         print("Job post added successfully!")

# #     elif choice == '2':
# #         user = career_page.User(career_page)
# #         jobs = user.view_jobs()
# #         for i, job in enumerate(jobs):
# #             print(f"{i}. {job['title']}")

# #         job_index = int(input("Enter the job index you want to apply for: "))
# #         if 0 <= job_index < len(jobs):
# #             user_info = {
# #                 "name": input("Enter your name: "),
# #                 "email": input("Enter your email: ")
# #             }
# #             result = user.apply_for_job(job_index, user_info)
# #             print(result)
# #         else:
# #             print("Invalid job index.")

# #     elif choice == '3':
# #         break

# class CareerPage:
#     def _init_(self):
#         self.job_posts = []
#         self.applications = []

#     class Admin:
#         def _init_(self, career_page):
#             self.career_page = career_page

#         def add_job_post(self, title, description):
#             job_post = {"title": title, "description": description}
#             self.career_page.job_posts.append(job_post)

#         def view_applications(self):
#             for application in self.career_page.applications:
#                 print("Application Details:", application)

#     class User:
#         def _init_(self, career_page):
#             self.career_page = career_page

#         def view_job_posts(self):
#             for index, job_post in enumerate(self.career_page.job_posts):
#                 print(f"Job {index + 1}: {job_post['title']} - {job_post['description']}")

#         def apply_for_job(self, user_name, job_index):
#             if job_index < 0 or job_index >= len(self.career_page.job_posts):
#                 print("Invalid job index")
#                 return

#             job_post = self.career_page.job_posts[job_index]
#             application = {"user_name": user_name, "job_title": job_post["title"]}
#             self.career_page.applications.append(application)
#             print(f"Application for '{job_post['title']}' submitted by {user_name}")




# career_page = CareerPage()
# admin = career_page.Admin(career_page)
# user = career_page.User(career_page)

# admin.add_job_post("Software Developer", "Looking for a software developer with experience in Python.")
# admin.add_job_post("Data Analyst", "Seeking a data analyst proficient in data analysis tools.")

# user.view_job_posts()
# user.apply_for_job("John", 0)
# admin.view_applications()