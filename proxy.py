from abc import ABC, abstractmethod

# Subject Interface
class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

# RealSubject (The real object that performs the actual work)
class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling the request.")

# Proxy (Controls access to RealSubject)
class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        if self._check_access():
            self._real_subject.request()
            self._log_access()
        else:
            print("Proxy: Access denied.")

    def _check_access(self) -> bool:
        print("Proxy: Checking access before forwarding the request.")
        # Add access control logic (e.g., authentication)
        return True  # Simulating access granted

    def _log_access(self):
        print("Proxy: Logging the request.")

# Client Code
def client_code(subject: Subject):
    subject.request()

# Usage
print("Using RealSubject directly:")
real_subject = RealSubject()
client_code(real_subject)

print("\nUsing Proxy to access RealSubject:")
proxy = Proxy(real_subject)
client_code(proxy)
