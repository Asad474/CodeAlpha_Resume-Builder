function showStep(stepNum) {
    $('.resume-form-details').each((index, step) => {
        if (index + 1 === stepNum) {
            $(step).css('display', 'block');
        } else {
            $(step).css('display', 'none');
        }
    });
}

$(document).ready(() => {
    const form = $('#resume-form');
    const nextBtns = form.find('.next-btn');
    const prevBtns = form.find('.prev-btn');
    const submitBtn = form.find('.submit-btn');
    let currentStep = 1;

    // Show the initial step on page load
    showStep(currentStep);

    // Hide the submit button initially
    submitBtn.hide();

    // Handle Next button clicks
    nextBtns.on('click', function (e) {
        e.preventDefault();
        currentStep++;
        showStep(currentStep);

        const totalSteps = $('.resume-form-details').length;

        // Show submit button only if current step is the last step
        if (currentStep === totalSteps) {
            submitBtn.show();
        } else {
            submitBtn.hide();
        }
    });

    // Handle Previous button clicks
    prevBtns.on('click', function (e) {
        e.preventDefault();
        currentStep--;
        showStep(currentStep);

        // Hide the submit button when navigating to previous steps
        submitBtn.hide();
    });

    const addNewForm = (container, template, selector, formName) => {
        const child = $(`${template}:last`).clone();
        let total_form = $(`#id_${formName}_set-TOTAL_FORMS`).val();
        const filtered_child = $(child).not(selector);
        filtered_child.find(':input:not([type=button]):not([type=submit]):not([type=reset])').each(function() {
            var name = $(this).attr('name').replace('-' + (total_form-1) + '-', '-' + total_form + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        });
        total_form++;
        $(container).find(selector).before(filtered_child);
        $(`#id_${formName}_set-TOTAL_FORMS`).val(total_form);
    };

    $('.add-education').on('click', (event) => {
        event.preventDefault();
        addNewForm('.cv-form-row-education', '.education-template', '.add-education', 'education');
    });

    $('.add-skill').on('click', (event) => {
        event.preventDefault();
        addNewForm('.cv-form-row-skills', '.skill-template', '.add-skill' ,'skill');
    });

    $('.add-experience').on('click', (event) => {
        event.preventDefault();
        addNewForm('.cv-form-row-experience', '.experience-template', '.add-experience');
    });

    $('.add-project').on('click', (event) => {
        event.preventDefault();
        addNewForm('.cv-form-row-project', '.project-template', '.add-project');
    });

    console.log($('.resumeform-section').html());
});