USERS = {
    "testuser": {
        "sn": "Testsson",
        "givenName": "Test",
        "eduPersonAffiliation": "student",
        "eduPersonScopedAffiliation": "student@se-leg.docker",
        "eduPersonPrincipalName": "testuser@se-leg.docker",
        "uid": "testuser",
        "eduPersonTargetedID": ["one!for!all"],
        "c": "SE",
        "o": "Example Co.",
        "ou": "IT",
        "initials": "P",
        "co": "co",
        "mail": "mail",
        "noreduorgacronym": "noreduorgacronym",
        "schacHomeOrganization": "se-leg.docker",
        "email": "test@example.com",
        "displayName": "Test Testsson",
        "labeledURL": "http://www.example.com/test My homepage",
        "norEduPersonNIN": "SE199012315555",
        "postaladdress": "postaladdress",
        "cn": "cn"
    },
    "roland": {
        "sn": "Hedberg",
        "givenName": "Roland",
        "eduPersonScopedAffiliation": "staff@example.com",
        "eduPersonPrincipalName": "rohe@example.com",
        "uid": "rohe",
        "eduPersonTargetedID": "one!for!all",
        "c": "SE",
        "o": "Example Co.",
        "ou": "IT",
        "initials": "P",
        # "schacHomeOrganization": "example.com",
        "mail": "roland@example.com",
        "displayName": "P. Roland Hedberg",
        "labeledURL": "http://www.example.com/rohe My homepage",
        "norEduPersonNIN": "SE197001012222"
    },
    "babs": {
        "surname": "Babs",
        "givenName": "Ozzie",
        "eduPersonAffiliation": "affiliate"
    },
    "upper": {
        "surname": "Jeter",
        "givenName": "Derek",
        "eduPersonAffiliation": "affiliate",
        "eduPersonScopedAffiliation": "affiliate@se-leg.docker",
        "eduPersonPrincipalName": "upper-eppn@se-leg.docker",
    },
}

EXTRA = {
    "roland": {
        "eduPersonEntitlement": "urn:mace:swamid.se:foo:bar",
        "schacGender": "male",
        "schacUserPresenceID": "skype:pepe.perez"
    },
    "upper": {
        "eduPersonEntitlement": "urn:mace:swamid.se:foo:bar",
        "schacGender": "male",
        "schacUserPresenceID": "skype:pepe.perez"
    }
}

