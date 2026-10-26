package com.contractplatform.service;

import com.contractplatform.domain.models.Client;
import com.contractplatform.domain.models.ClientUserDetails;
import com.contractplatform.repository.ClientRepository;
import lombok.RequiredArgsConstructor;
import org.jspecify.annotations.NullMarked;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
@RequiredArgsConstructor
public class ClientUserDetailsService implements UserDetailsService {

    private final ClientRepository clientRepository;

    @Override
    @NullMarked
    public UserDetails loadUserByUsername(String email) throws UsernameNotFoundException {

        Optional<Client> optClient = clientRepository.findByEmail(email);

        if (optClient.isEmpty()) {
            throw new UsernameNotFoundException("Client with: " + email + " not found.");
        }

        Client client = optClient.get();
        return new ClientUserDetails(client);
    }
}
