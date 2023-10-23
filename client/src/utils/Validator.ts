import LoanSwift from "../interfaces/LoanSwift";
import Joi from "joi";

class Validator {
    public isLoanSwift(formPayload:LoanSwift) {
        const validator = Joi.object({
            document_number: Joi.number().min(1).required(),
            first_name: Joi.string().pattern(new RegExp('^[a-zA-Z]*$')).required(),
            last_name: Joi.string().pattern(new RegExp('^[a-zA-Z]*$')).required(),
            gender: Joi.string().valid("Male", "Female", "Non-binary").required(),
            email: Joi.string().email({ tlds: { allow: false } }).required(),
            amount: Joi.number().min(1).required()
        })
        const isValidate = validator.validate(formPayload);
        if (isValidate.error) {
            console.log(isValidate.error)
            return false
        }
        return true
    }
}

export default (new Validator)