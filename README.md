# certiGenerator

Now easily generate participation certificates digitally using this package.

The package takes following six inputs --
1. Certificate template path
2. Organization's logo
3. Participant's name
4. Event name
5. Organization name
6. Issuer name
7. Output path 

# Sample Code

import certiGenerator <br />
api = certiGenerator.certificateGenerator()

api.generate_certificate("certificate_template.png","google.png","Yatharth Arora","Software Development","Google","Google India","test.jpg")
