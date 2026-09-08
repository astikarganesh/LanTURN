import os

base = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app\ui\screens\employer"
os.makedirs(base, exist_ok=True)

home_vm = '''package com.lanturn.app.ui.screens.employer

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.lanturn.app.data.models.EmployerProfileDto
import com.lanturn.app.data.models.JobDto
import com.lanturn.app.data.network.ApiResult
import com.lanturn.app.data.repositories.EmployerRepository
import com.lanturn.app.data.repositories.JobRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

data class EmployerHomeState(
    val isLoading: Boolean = false,
    val profile: EmployerProfileDto? = null,
    val jobs: List<JobDto> = emptyList(),
    val error: String? = null,
    val totalApplicants: Int = 0 // Mock stat for now
)

class EmployerHomeViewModel(
    private val employerRepo: EmployerRepository,
    private val jobRepo: JobRepository
) : ViewModel() {

    private val _state = MutableStateFlow(EmployerHomeState())
    val state: StateFlow<EmployerHomeState> = _state.asStateFlow()

    init {
        loadDashboardData()
    }

    fun loadDashboardData() {
        _state.update { it.copy(isLoading = true, error = null) }
        
        viewModelScope.launch {
            // Load Profile
            employerRepo.getProfile().collect { result ->
                when (result) {
                    is ApiResult.Success -> {
                        _state.update { it.copy(profile = result.data, isLoading = false) }
                    }
                    is ApiResult.Error -> {
                        _state.update { it.copy(error = result.message, isLoading = false) }
                    }
                }
            }
        }
        
        viewModelScope.launch {
            // Load Recent Jobs
            jobRepo.getJobs(limit = 5).collect { result ->
                if (result is ApiResult.Success) {
                    _state.update { it.copy(jobs = result.data.data) }
                }
            }
        }
    }
}
'''

jobs_vm = '''package com.lanturn.app.ui.screens.employer

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.lanturn.app.data.models.JobCreateRequest
import com.lanturn.app.data.models.JobDto
import com.lanturn.app.data.network.ApiResult
import com.lanturn.app.data.repositories.JobRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

data class EmployerJobsState(
    val isLoading: Boolean = false,
    val isSaving: Boolean = false,
    val jobs: List<JobDto> = emptyList(),
    val error: String? = null,
    val saveError: String? = null
)

class EmployerJobsViewModel(
    private val repository: JobRepository
) : ViewModel() {

    private val _state = MutableStateFlow(EmployerJobsState())
    val state: StateFlow<EmployerJobsState> = _state.asStateFlow()

    init {
        loadJobs()
    }

    fun loadJobs() {
        _state.update { it.copy(isLoading = true, error = null) }
        viewModelScope.launch {
            repository.getJobs(limit = 20).collect { result ->
                when (result) {
                    is ApiResult.Success -> {
                        _state.update { it.copy(jobs = result.data.data, isLoading = false) }
                    }
                    is ApiResult.Error -> {
                        _state.update { it.copy(error = result.message, isLoading = false) }
                    }
                }
            }
        }
    }
    
    fun createJob(request: JobCreateRequest, onComplete: (Boolean) -> Unit) {
        _state.update { it.copy(isSaving = true, saveError = null) }
        viewModelScope.launch {
            repository.createJob(request).collect { result ->
                when (result) {
                    is ApiResult.Success -> {
                        _state.update { it.copy(isSaving = false) }
                        loadJobs()
                        onComplete(true)
                    }
                    is ApiResult.Error -> {
                        _state.update { it.copy(isSaving = false, saveError = result.message) }
                        onComplete(false)
                    }
                }
            }
        }
    }
}
'''

profile_vm = '''package com.lanturn.app.ui.screens.employer

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.lanturn.app.data.models.EmployerProfileDto
import com.lanturn.app.data.network.ApiResult
import com.lanturn.app.data.repositories.EmployerRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

data class EmployerProfileState(
    val isLoading: Boolean = false,
    val isSaving: Boolean = false,
    val profile: EmployerProfileDto? = null,
    val error: String? = null,
    val saveError: String? = null
)

class EmployerProfileViewModel(
    private val repository: EmployerRepository
) : ViewModel() {

    private val _state = MutableStateFlow(EmployerProfileState())
    val state: StateFlow<EmployerProfileState> = _state.asStateFlow()

    init {
        loadProfile()
    }

    fun loadProfile() {
        _state.update { it.copy(isLoading = true, error = null) }
        viewModelScope.launch {
            repository.getProfile().collect { result ->
                when (result) {
                    is ApiResult.Success -> {
                        _state.update { it.copy(profile = result.data, isLoading = false) }
                    }
                    is ApiResult.Error -> {
                        _state.update { it.copy(error = result.message, isLoading = false) }
                    }
                }
            }
        }
    }

    fun updateProfile(profile: EmployerProfileDto, onSuccess: () -> Unit) {
        _state.update { it.copy(isSaving = true, saveError = null) }
        viewModelScope.launch {
            repository.updateProfile(profile).collect { result ->
                when (result) {
                    is ApiResult.Success -> {
                        _state.update { it.copy(profile = result.data, isSaving = false) }
                        onSuccess()
                    }
                    is ApiResult.Error -> {
                        _state.update { it.copy(saveError = result.message, isSaving = false) }
                    }
                }
            }
        }
    }
}
'''

apps_vm = '''package com.lanturn.app.ui.screens.employer

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.lanturn.app.data.models.ApplicationDto
import com.lanturn.app.data.models.ApplicationStatus
import com.lanturn.app.data.models.ApplicationStatusUpdateRequest
import com.lanturn.app.data.network.ApiResult
import com.lanturn.app.data.repositories.ApplicationRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

data class EmployerApplicantsState(
    val isLoading: Boolean = false,
    val applications: List<ApplicationDto> = emptyList(),
    val error: String? = null,
    val isUpdating: Boolean = false,
    val updateError: String? = null
)

class EmployerApplicantsViewModel(
    private val repository: ApplicationRepository
) : ViewModel() {

    private val _state = MutableStateFlow(EmployerApplicantsState())
    val state: StateFlow<EmployerApplicantsState> = _state.asStateFlow()

    fun loadApplications(jobId: String? = null) {
        _state.update { it.copy(isLoading = true, error = null) }
        viewModelScope.launch {
            repository.getEmployerApplications(jobId = jobId).collect { result ->
                when (result) {
                    is ApiResult.Success -> {
                        _state.update { it.copy(applications = result.data.data, isLoading = false) }
                    }
                    is ApiResult.Error -> {
                        _state.update { it.copy(error = result.message, isLoading = false) }
                    }
                }
            }
        }
    }
    
    fun updateApplicationStatus(applicationId: String, status: ApplicationStatus, notes: String? = null) {
        _state.update { it.copy(isUpdating = true, updateError = null) }
        viewModelScope.launch {
            repository.updateApplicationStatus(applicationId, ApplicationStatusUpdateRequest(status, notes)).collect { result ->
                when (result) {
                    is ApiResult.Success -> {
                        // Update local list
                        val updatedList = _state.value.applications.map { 
                            if (it.id == applicationId) result.data else it 
                        }
                        _state.update { it.copy(applications = updatedList, isUpdating = false) }
                    }
                    is ApiResult.Error -> {
                        _state.update { it.copy(updateError = result.message, isUpdating = false) }
                    }
                }
            }
        }
    }
}
'''

with open(os.path.join(base, "EmployerHomeViewModel.kt"), "w", encoding="utf-8") as f:
    f.write(home_vm)
with open(os.path.join(base, "EmployerJobsViewModel.kt"), "w", encoding="utf-8") as f:
    f.write(jobs_vm)
with open(os.path.join(base, "EmployerProfileViewModel.kt"), "w", encoding="utf-8") as f:
    f.write(profile_vm)
with open(os.path.join(base, "EmployerApplicantsViewModel.kt"), "w", encoding="utf-8") as f:
    f.write(apps_vm)