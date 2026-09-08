import os

base_dir = r"C:\Users\Aravind\Downloads\clg projects\lanturn-kotlin\app\src\main\java\com\lanturn\app"

# 1. AiModels.kt
ai_models_path = os.path.join(base_dir, "data", "models", "AiModels.kt")
ai_models_content = """package com.lanturn.app.data.models

import kotlinx.serialization.Serializable

@Serializable
data class CareerChatRequest(
    val message: String,
    val threadId: String? = null,
    val mode: String? = "career_guidance",
    val jobId: String? = null
)

@Serializable
data class CareerChatResponse(
    val threadId: String,
    val reply: String
)

@Serializable
data class ChatMessageDto(
    val messageId: String? = null,
    val role: String, // 'user' or 'assistant'
    val content: String,
    val createdAt: String? = null
)

@Serializable
data class ChatThreadDto(
    val threadId: String,
    val title: String? = null,
    val mode: String? = null,
    val updatedAt: String? = null
)
"""

# 2. AiApi.kt
ai_api_path = os.path.join(base_dir, "data", "api", "AiApi.kt")
ai_api_content = """package com.lanturn.app.data.api

import com.lanturn.app.data.models.CareerChatRequest
import com.lanturn.app.data.models.CareerChatResponse
import com.lanturn.app.data.models.ChatMessageDto
import com.lanturn.app.data.models.ChatThreadDto
import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.Path

interface AiApi {
    @POST("ai/career-chat")
    suspend fun careerChat(@Body request: CareerChatRequest): Response<ApiResponse<CareerChatResponse>>

    @GET("ai/threads")
    suspend fun getThreads(): Response<ApiResponse<List<ChatThreadDto>>>

    @GET("ai/threads/{threadId}/messages")
    suspend fun getThreadMessages(@Path("threadId") threadId: String): Response<ApiResponse<List<ChatMessageDto>>>
}
"""

# 3. AiRepository.kt
ai_repo_path = os.path.join(base_dir, "data", "repositories", "AiRepository.kt")
ai_repo_content = """package com.lanturn.app.data.repositories

import com.lanturn.app.data.api.AiApi
import com.lanturn.app.data.models.CareerChatRequest
import com.lanturn.app.data.models.CareerChatResponse
import com.lanturn.app.data.models.ChatMessageDto
import com.lanturn.app.data.models.ChatThreadDto
import com.lanturn.app.data.network.ApiResult
import com.lanturn.app.data.network.safeApiCall
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flow
import kotlinx.coroutines.flow.flowOn

class AiRepository(private val api: AiApi) {

    fun careerChat(request: CareerChatRequest): Flow<ApiResult<CareerChatResponse>> = flow {
        emit(safeApiCall { api.careerChat(request) })
    }.flowOn(Dispatchers.IO)

    fun getThreads(): Flow<ApiResult<List<ChatThreadDto>>> = flow {
        emit(safeApiCall { api.getThreads() })
    }.flowOn(Dispatchers.IO)

    fun getThreadMessages(threadId: String): Flow<ApiResult<List<ChatMessageDto>>> = flow {
        emit(safeApiCall { api.getThreadMessages(threadId) })
    }.flowOn(Dispatchers.IO)
}
"""

# 4. CareerAiViewModel.kt
ai_vm_path = os.path.join(base_dir, "ui", "screens", "student", "CareerAiViewModel.kt")
ai_vm_content = """package com.lanturn.app.ui.screens.student

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.lanturn.app.data.models.CareerChatRequest
import com.lanturn.app.data.models.ChatMessageDto
import com.lanturn.app.data.network.ApiResult
import com.lanturn.app.data.repositories.AiRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

data class CareerAiState(
    val isLoading: Boolean = false,
    val messages: List<ChatMessageDto> = emptyList(),
    val currentThreadId: String? = null,
    val error: String? = null,
    val inputText: String = ""
)

class CareerAiViewModel(private val repository: AiRepository) : ViewModel() {
    private val _state = MutableStateFlow(CareerAiState())
    val state: StateFlow<CareerAiState> = _state.asStateFlow()

    init {
        // Start with a greeting message
        _state.update {
            it.copy(
                messages = listOf(
                    ChatMessageDto(
                        role = "assistant",
                        content = "Hi! I'm your LanTURN AI Career Assistant. How can I help you with your career today?"
                    )
                )
            )
        }
    }

    fun onInputTextChanged(text: String) {
        _state.update { it.copy(inputText = text) }
    }

    fun sendMessage() {
        val text = _state.value.inputText.trim()
        if (text.isEmpty() || _state.value.isLoading) return

        // Add user message locally
        val userMessage = ChatMessageDto(role = "user", content = text)
        _state.update {
            it.copy(
                messages = it.messages + userMessage,
                inputText = "",
                isLoading = true,
                error = null
            )
        }

        viewModelScope.launch {
            val request = CareerChatRequest(
                message = text,
                threadId = _state.value.currentThreadId
            )
            repository.careerChat(request).collect { result ->
                when (result) {
                    is ApiResult.Success -> {
                        val aiMessage = ChatMessageDto(
                            role = "assistant",
                            content = result.data.reply
                        )
                        _state.update {
                            it.copy(
                                messages = it.messages + aiMessage,
                                currentThreadId = result.data.threadId,
                                isLoading = false
                            )
                        }
                    }
                    is ApiResult.Error -> {
                        _state.update { it.copy(error = result.message, isLoading = false) }
                    }
                    is ApiResult.Exception -> {
                        _state.update { it.copy(error = result.e.message, isLoading = false) }
                    }
                }
            }
        }
    }
}
"""

with open(ai_models_path, "w", encoding="utf-8") as f:
    f.write(ai_models_content)
with open(ai_api_path, "w", encoding="utf-8") as f:
    f.write(ai_api_content)
with open(ai_repo_path, "w", encoding="utf-8") as f:
    f.write(ai_repo_content)
with open(ai_vm_path, "w", encoding="utf-8") as f:
    f.write(ai_vm_content)