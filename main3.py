import google.generativeai as genai

genai.configure(api_key="")    #API key needed
model = genai.GenerativeModel("gemini-2.0-flash-lite")
class TechLearningPathGenerator:
    def __init__(self):
        self.domains_dict = {
            "soft dev": ["python", "C++", "java", "C#", "Django", "Flask", "Spring Boot", ".NET", "FastAPI"],
            "web dev": ["HTML", "CSS", "JavaScript", "Python", "TypeScript", "PHP", "React", "Vue.js", "Angular", "Django", "Flask", "Node.js", "Express"],
            "ds ml": ["Python", "R", "SQL", "NumPy", "Pandas", "Scikit-learn", "TensorFlow", "PyTorch", "Matplotlib", "Seaborn"],
            "app dev": ["Kotlin", "Swift", "Dart", "Java", "JavaScript", "Flutter", "React Native", "SwiftUI", "Jetpack Compose"],
            "devops": ["Python", "Go", "Bash", "YAML", "Docker", "Kubernetes", "Terraform", "Jenkins", "Ansible", "GitHub Actions"],
            "cyber sec": ["Python", "C", "C++", "JavaScript", "Metasploit", "Nmap", "Wireshark", "Burp Suite", "Scapy"],
            "game dev": ["C#", "C++", "Python", "JavaScript", "Unity", "Unreal Engine", "Godot", "Pygame"],
        }

    def get_required_technologies(self, domain, known_technologies):
        if domain not in self.domains_dict:
            raise ValueError(f"Domain not found. Available domains: {', '.join(self.domains_dict.keys())}")
        known_tech_lower = [tech.lower() for tech in known_technologies]
        
        required_techs = []
        for tech in self.domains_dict[domain]:
            if tech.lower() not in known_tech_lower:
                required_techs.append(tech)
                
        return required_techs

    def get_youtube_links(self, technologies):
        """Generate YouTube search links for the given technologies."""
        youtube_links = []
        
        # Create search links without channel preference
        for tech in technologies:
            response = model.generate_content(f"provide me with only ONE direct YouTube video link for the best tutorial about {tech} from either freeCodeCamp, Bro Code, or LearnCode Academy. Format your response as just the complete YouTube URL with absolutely nothing else - no descriptions, no explanations, just the plain URL leading directly to the tutorial video. For example:https://www.youtube.com/watch?v=VideoID")
            youtube_links.append(response.text)
        return youtube_links


def main():
    """Main function to generate YouTube learning resources."""
    generator = TechLearningPathGenerator()
    
    # Get user inputs
    print("Available domains:", ", ".join(generator.domains_dict.keys()))
    domain = input("Enter your desired domain: ")
    known_tech_input = input("Enter the technologies you already know (comma-separated): ")
    known_technologies = [tech.strip() for tech in known_tech_input.split(",") if tech.strip()]
    
    try:
        # Get required technologies and YouTube links
        required_techs = generator.get_required_technologies(domain, known_technologies)
        youtube_links = generator.get_youtube_links(required_techs)
        
        # Display results
        print(required_techs)
        print(youtube_links)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()