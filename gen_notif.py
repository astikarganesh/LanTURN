import os

base_dir = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app"

# 1. NotificationModels.kt
models_path = os.path.join(base_dir, "data", "models", "NotificationModels.kt")
models_content = """package com.lanturn.app.data.models

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonObject

@Serializable
data class NotificationDto(
    val id: String,
    val userId: String,
    val type: String,
    val title: String,
    val body: String,
    val link: String? = null,
    val read: Boolean,
    val channel: String? = null,
    val createdAt: String,
    val updatedAt: String
)

@Serializable
data class UnreadCountDto(
    val count: Int
)

@Serializable
data class GenericOkResponse(
    val ok: Boolean
)
"""

# 2. NotificationApi.kt
api_path = os.path.join(base_dir, "data", "api", "NotificationApi.kt")
api_content = """package com.lanturn.app.data.api

import com.lanturn.app.data.models.GenericOkResponse
import com.lanturn.app.data.models.NotificationDto
import com.lanturn.app.data.models.PaginatedResponse
import com.lanturn.app.data.models.UnreadCountDto
import retrofit2.http.GET
import retrofit2.http.PATCH
import retrofit2.http.POST
import retrofit2.http.Path
import retrofit2.http.Query
import kotlinx.serialization.Serializable

@Serializable
data class NotificationPaginatedResponse(
    val items: List<NotificationDto>
)

@Serializable
data class NotificationBaseResponse<T>(
    val data: T
)

interface NotificationApi {
    @GET("notifications")
    suspend fun getNotifications(@Query("limit") limit: Int = 50): NotificationBaseResponse<NotificationPaginatedResponse>

    @GET("notifications/unread-count")
    suspend fun getUnreadCount(): NotificationBaseResponse<UnreadCountDto>

    @PATCH("notifications/{id}/read")
    suspend fun markRead(@Path("id") id: String): NotificationBaseResponse<GenericOkResponse>

    @POST("notifications/read-all")
    suspend fun markAllRead(): NotificationBaseResponse<GenericOkResponse>
}
"""

# 3. NotificationRepository.kt
repo_path = os.path.join(base_dir, "data", "repositories", "NotificationRepository.kt")
repo_content = """package com.lanturn.app.data.repositories

import com.lanturn.app.data.api.NotificationApi
import com.lanturn.app.data.models.NotificationDto
import com.lanturn.app.data.network.ApiResult
import com.lanturn.app.data.network.safeApiCall
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flow
import kotlinx.coroutines.flow.flowOn

class NotificationRepository(private val api: NotificationApi) {

    fun getNotifications(limit: Int = 50): Flow<ApiResult<List<NotificationDto>>> = flow {
        emit(safeApiCall { api.getNotifications(limit).data.items })
    }.flowOn(Dispatchers.IO)

    fun getUnreadCount(): Flow<ApiResult<Int>> = flow {
        emit(safeApiCall { api.getUnreadCount().data.count })
    }.flowOn(Dispatchers.IO)

    fun markRead(id: String): Flow<ApiResult<Boolean>> = flow {
        emit(safeApiCall { api.markRead(id).data.ok })
    }.flowOn(Dispatchers.IO)

    fun markAllRead(): Flow<ApiResult<Boolean>> = flow {
        emit(safeApiCall { api.markAllRead().data.ok })
    }.flowOn(Dispatchers.IO)
}
"""

# 4. NotificationViewModel.kt
vm_path = os.path.join(base_dir, "ui", "screens", "NotificationViewModel.kt")
vm_content = """package com.lanturn.app.ui.screens

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.lanturn.app.data.models.NotificationDto
import com.lanturn.app.data.network.ApiResult
import com.lanturn.app.data.repositories.NotificationRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

data class NotificationState(
    val isLoading: Boolean = false,
    val notifications: List<NotificationDto> = emptyList(),
    val unreadCount: Int = 0,
    val error: String? = null
)

class NotificationViewModel(private val repository: NotificationRepository) : ViewModel() {
    private val _state = MutableStateFlow(NotificationState())
    val state: StateFlow<NotificationState> = _state.asStateFlow()

    init {
        loadNotifications()
    }

    fun loadNotifications() {
        _state.update { it.copy(isLoading = true, error = null) }
        viewModelScope.launch {
            repository.getNotifications().collect { result ->
                when (result) {
                    is ApiResult.Success -> {
                        val unreadCount = result.data.count { !it.read }
                        _state.update { it.copy(notifications = result.data, unreadCount = unreadCount, isLoading = false) }
                    }
                    is ApiResult.Error -> _state.update { it.copy(error = result.message, isLoading = false) }
                    is ApiResult.Exception -> _state.update { it.copy(error = result.e.message, isLoading = false) }
                }
            }
        }
    }
    
    fun fetchUnreadCount() {
        viewModelScope.launch {
            repository.getUnreadCount().collect { result ->
                if (result is ApiResult.Success) {
                    _state.update { it.copy(unreadCount = result.data) }
                }
            }
        }
    }

    fun markAsRead(id: String) {
        // Optimistic update
        val updatedList = _state.value.notifications.map { 
            if (it.id == id) it.copy(read = true) else it 
        }
        val unreadCount = updatedList.count { !it.read }
        _state.update { it.copy(notifications = updatedList, unreadCount = unreadCount) }
        
        viewModelScope.launch {
            repository.markRead(id).collect { /* handle if error */ }
        }
    }
    
    fun markAllAsRead() {
        val updatedList = _state.value.notifications.map { it.copy(read = true) }
        _state.update { it.copy(notifications = updatedList, unreadCount = 0) }
        
        viewModelScope.launch {
            repository.markAllRead().collect { /* handle if error */ }
        }
    }
}
"""

with open(models_path, "w", encoding="utf-8") as f:
    f.write(models_content)
with open(api_path, "w", encoding="utf-8") as f:
    f.write(api_content)
with open(repo_path, "w", encoding="utf-8") as f:
    f.write(repo_content)
with open(vm_path, "w", encoding="utf-8") as f:
    f.write(vm_content)