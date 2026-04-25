def apply_rules(data):
    enriched = str(data)

    # Rule 1: Login related scenarios
    if "login" in enriched.lower():
        enriched += "\n- Test invalid login attempts"
        enriched += "\n- Test session timeout"
        enriched += "\n- Test password reset flow"

    # Rule 2: File upload scenarios
    if "upload" in enriched.lower():
        enriched += "\n- Test file format validation"
        enriched += "\n- Test max file size"
        enriched += "\n- Test corrupted file upload"

    # Rule 3: User roles
    if "admin" in enriched.lower():
        enriched += "\n- Test admin access control"
        enriched += "\n- Test privilege escalation"

    return enriched
