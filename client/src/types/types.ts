export interface InterfaceVacancy {
	id: string
	premium: boolean
	billing_type: BillingType
	relations: any[]
	name: string
	insider_interview: any
	response_letter_required: boolean
	area: Area
	salary: Salary | null
	type: Type
	address: any
	allow_messages: boolean
	experience: Experience
	schedule: Schedule
	employment: Employment
	department: any
	contacts: any
	description: string
	branded_description: any
	vacancy_constructor_template: any
	key_skills: KeySkill[]
	accept_handicapped: boolean
	accept_kids: boolean
	archived: boolean
	response_url: any
	specializations: any[]
	professional_roles: ProfessionalRole[]
	code: any
	hidden: boolean
	quick_responses_allowed: boolean
	driver_license_types: any[]
	accept_incomplete_resumes: boolean
	employer: Employer
	published_at: string
	created_at: string
	initial_created_at: string
	negotiations_url: any
	suitable_resumes_url: any
	apply_alternate_url: string
	has_test: boolean
	test: any
	alternate_url: string
	working_days: any[]
	working_time_intervals: any[]
	working_time_modes: any[]
	accept_temporary: boolean
	languages: any[]
	added_at: Date
	status: 'waiting' | 'accepted' | 'rejected'
}

export interface BillingType {
	id: string
	name: string
}

export interface Area {
	id: string
	name: string
	url: string
}

export interface Salary {
	from: number | null
	to: number | null
	currency: string
	gross: boolean
}

export interface Type {
	id: string
	name: string
}

export interface Experience {
	id: string
	name: string
}

export interface Schedule {
	id: string
	name: string
}

export interface Employment {
	id: string
	name: string
}

export interface KeySkill {
	name: string
}

export interface ProfessionalRole {
	id: string
	name: string
}

export interface Employer {
	id: string
	name: string
	url: string
	alternate_url: string
	logo_urls: LogoUrls
	vacancies_url: string
	accredited_it_employer: boolean
	trusted: boolean
}

export interface LogoUrls {
	'90': string
	'240': string
	original: string
}

export interface InterfaceResponse {
	clientId: string
	client_id: string
	credential: string
	select_by: string
}

export interface InterfaceUser {
	iss: string
	azp: string
	aud: string
	sub: string
	email: string
	email_verified: boolean
	nbf: number
	name: string
	picture: string
	given_name: string
	locale: string
	iat: number
	exp: number
	jti: string
}

export interface InterfaceUserDB {
	name: string
	email: string
	sub: string
}

export interface InterfaceVacancyDB {
	text: string
	user_id: number
}
